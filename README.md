# wallpaper-engine-kde-personal
Steps to reproduce an rpm of the project wallpaper-engine-kde by Catsout on an Immutable OS (Aurora/Bazzite):

1. Create a container to install the dependencies necessary to build the rpm. In a terminal run:
   
podman run -it docker.io/library/fedora

For ublue-OS's, the containers are stored in /var/home/$USER/.local/share/containers/storage/overlay. There will be a couple folders here, take note of the one which has been modified most recently.

2.  Going back to the terminal with the running container. First install all the necessary dependencies:
   
sudo dnf install mpv-libs-devel vulkan-headers plasma-workspace-devel kf5-plasma-devel lz4-devel qt5-qtbase-private-devel qt5-qtx11extras-devel plasma-workspace gstreamer1-libav mpv-libs lz4 python3-websockets qt5-qtwebchannel-devel qt5-qtwebsockets-devel git rpmdevtools nano

Secondly, clone the github repo like so:

github clone --branch qt6 https://github.com/catsout/wallpaper-engine-kde-plugin 

And move into it and run these commands: \
cd wallpaper-engine-kde-plugin \
git submodule update --init --recursive \
kpackagetool5 -i ./plugin 

3. We now need to edit the rpm install script, as it is outdated. Enter the command:

nano rpm/wek.spec

Once open, refer to the spec file attached above to this repository. Simply, delete everything currently in the containers .spec file, and replace it with this repo's spec contents.

4. Run the rpm build file:

rpmbuild --define="commit $(git rev-parse HEAD)" \
    --define="glslang_ver 11.8.0" \
    --undefine=_disable_source_fetch \
    -ba ./rpm/wek.spec

5. Exiting the container, we shall now go to the location of the container file on our Host OS, mentioned above. (/var/home/$USER/.local/share/containers/storage/overlay). Once you've found the correct container folder, open it, and navigate to:

{container-location}/diff/root/rpmbuild/RPMS/x86_64 

6. Here lies our RPM file we need. Copy it, and paste it anywhere you please, I placed it in my Downloads folder. Open the terminal in the location of the RPM package, and run:

rpm-ostree install {RPM_FILE_NAME}.rpm

Before rebooting, we also need to copy the plugins folder from the Wallpaper-engine-kde-plugin repository. First, create a folder like so:

mkdir /var/home/$USER/.local/share/plasma/wallpapers/com.github.catsout.wallpaperEngineKde

Lastly, you can use the already cloned repository from our container (diff/wallpaper-engine-kde-plugin), and from it you need these files/folders from the plugins folder: contents folder, metadata.desktop and metadata.json. And just move those files/folder into the previously created folder.

Now reboot your machine, and hopefully when you go to the wallpapers setting, under Wallpaper type, should be Wallpaper Engine for KDE!


