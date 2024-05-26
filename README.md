# wallpaper-engine-kde-personal
Steps to reproduce an rpm of the project wallpaper-engine-kde by Catsout on an Immutable OS (Aurora/Bazzite):

1.) Create a container to install the dependencies necessary to build the rpm. In a terminal run: \n podman run -it docker.io/library/fedora
\n For ublue-OS's, the containers are stored in /var/home/$USER/.local/share/containers/storage/overlay. The folder you'll need in a couple steps is the latest one that's been modified.

3.) Going back to the terminal with the running container.
First install all the necessary dependencies:
\n sudo dnf install mpv-libs-devel vulkan-headers plasma-workspace-devel kf5-plasma-devel lz4-devel qt5-qtbase-private-devel qt5-qtx11extras-devel plasma-workspace gstreamer1-libav mpv-libs lz4 python3-websockets qt5-qtwebchannel-devel qt5-qtwebsockets-devel git rpmdevtools nano

Secondly, clone the github repo like so: 
github clone --branch qt6 https://github.com/catsout/wallpaper-engine-kde-plugin
And move into it: 
\n cd wallpaper-engine-kde-plugin
\n git submodule update --init --recursive
And run:
\n kpackagetool5 -i ./plugin

4.) We now need to edit the rpm install script, as it is outdated.
Enter the command \n nano rpm/wek.spec
Once open refer to the spec file attached above to this repository. Simply, delete everything currently in the containers .spec file, and replace it with this repository spec contents.

5.) Run the rpm build file:
\n rpmbuild --define="commit $(git rev-parse HEAD)" \
    --define="glslang_ver 11.8.0" \
    --undefine=_disable_source_fetch \
    -ba ./rpm/wek.spec

6.) Exiting the container, we shall now go to the location of the container file on our Host OS, mentioned above. (/var/home/$USER/.local/share/containers/storage/overlay). Once you've found the correct container folder, open it, and navigate to: diff/root/rpmbuild/RPMS/x86_64

7. Here lies our RPM file we need. Copy it, and paste it anywhere you please, I placed it in my Downloads folder. Open the terminal of the location of the RPM package, and run \n rpm-ostree install <wallpaper-engine-kde-plugin>.rpm
Before rebooting, we also need to copy the plugins folder from the Wallpaper-engine-kde-plugin repository. First, create a folder like so:
\n mkdir /var/home/$USER/.local/share/plasma/wallpapers/com.github.catsout.wallpaperEngineKde.
\n Lastly, you can use the already cloned repository from our container, and from it you need these files/folders from the plugins folder: contents folder, metadata.desktop and metadata.json. And just move those files/folder into the previously created folder.

Now reboot your machine, and hopefully when you go to the wallpapers setting, under Wallpaper type, should be Wallpaper Engine for Kde!


