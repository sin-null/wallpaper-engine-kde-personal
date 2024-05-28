# wallpaper-engine-kde-personal
Steps to reproduce an rpm of the project wallpaper-engine-kde by Catsout on an Immutable OS (Aurora Tested): \
READ: IF YOU ARE ON BAZZITE AND ARE HAVING ISSUES WITH PACKAGE CONFLICTS INVOLVING MESA READ THESE FORUM POSTS: \
https://universal-blue.discourse.group/t/how-to-install-wallpaper-engine-on-bazzite-3/1894/16 \
NOTE: In the future Catsout repository might merge the QT6 branch and Main branch, so if that happens edit the .spec file here, and remove the --branch qt6 part of the git clone. 

1. Create a container to install the dependencies necessary to build the rpm. In a terminal run:
   
podman run -it docker.io/library/fedora

For ublue-OS's, the containers are stored in /var/home/$USER/.local/share/containers/storage/overlay. There will be a couple folders here, take note of the one which has been modified most recently.

2.  Going back to the terminal with the running container. First install all the necessary dependencies:
   
sudo dnf install mpv-libs-devel vulkan-headers plasma-workspace-devel libplasma-devel lz4-devel qt6-qtbase-private-devel qt6-qtdeclarative-devel git nano rpmdevtools extra-cmake-modules

Secondly, clone the github repo to get my .spec file and clone Catsout repository, as we'll need their plugins folder later:

mkdir build_wallpaper_rpm && cd build_wallpaper_rpm \
git clone https://github.com/Broken-Void/wallpaper-engine-kde-personal.git \
git clone --single-branch --branch qt6 https://github.com/catsout/wallpaper-engine-kde-plugin.git && cd wallpaper-engine-kde-plugin && git submodule update --init --recursive && cd .. \
mv -v  wallpaper-engine-kde-plugin/plugin/* ./ && rm -rf wallpaper-engine-kde-plugin

And move into my repository: \
cd wallpaper-engine-kde-personal 

3. Create rpmbuilds folder and run the rpm build file:

rpmdev-setuptree \
rpmbuild --define="commit $(git rev-parse HEAD)" --undefine=_disable_source_fetch -ba ./wek.spec 

4. Exiting the container, we shall now go to the location of the container file on our Host OS, mentioned above. (/var/home/$USER/.local/share/containers/storage/overlay). Once you've found the correct container folder, open it, and navigate to:

{container-location}/diff/root/rpmbuild/RPMS/x86_64 

5. Here lies our RPM file we need. Copy it, and paste it anywhere you please, I placed it in my Downloads folder. Open the terminal in the location of the RPM package, and run:

rpm-ostree install {RPM_FILE_NAME}.rpm

Before rebooting, we also need to create a plugins folder:

mkdir /var/home/$USER/.local/share/plasma/wallpapers/com.github.catsout.wallpaperEngineKde

Lastly, go back to the container folder, build_wallpaper_rpm we created (diff/build_wallpaper_rpm) in the 2nd step, and from it you need to move these files/folders : contents folder, metadata.desktop and metadata.json. And put those files/folder into the folder created before.

Now reboot your machine, and hopefully when you go to the wallpapers setting, under Wallpaper type, should be Wallpaper Engine for KDE! Feel free to delete the container as well with: podman rmi -f fedora

Based off of this repository: https://github.com/KyleGospo/wallpaper-engine-kde-plugin , I was able to create a working .spec file. \
Package this repository is created for: https://github.com/catsout/wallpaper-engine-kde-plugin


