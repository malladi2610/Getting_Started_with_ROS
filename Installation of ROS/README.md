# Installation of ROS

#### Steps to be followed are
- Setup your computer to accept software from packages.ros.org : 
```sh
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```
- Set up your keys.
```sh
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```

- Make sure your Debian package index is up-to-date.
```sh
sudo apt update
```

- Installing the ROS recommended configuration.
```sh
sudo apt install ros-melodic-desktop-full
```
 
- Configuration Steps : 
Adding environment variables: To Automatically add ROS environment variables to your bash session every time a new shell (terminal) is launched, enter the following commands (this step is similar as adding environmental variable in windows):
```sh
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

- Initialize rosdep: Before you can use many ROS tools, you will need to initialize rosdep. rosdep enables you to easily install system dependencies for source you want to compile and is required to run some core components in ROS.
```sh
sudo apt install python-rosdep
sudo rosdep init
rosdep update
```

- More packages to install :
1) Catkin Tools
```sh
sudo apt-get install ros-melodic-catkin python-catkin-tools
```
2) std_msg package
```sh
sudo apt install ros-melodic-std-msgs
```
3) turtlesim
```sh
sudo apt-get install ros-melodic-ros-tutorials
```

- Creating a workspace
1) Open up the terminal
2) And now we are going to a catkin workspace. It can be named anything but in general, it is named as catkin_ws
The commands to do so are

```sh
cd ~/
mkdir --parents catkin_ws/src
cd catkin_ws
```
- Now the workspace created above needs to be initialized
```sh
catkin init
```
This commands creates your workspace

- Now once the workspace is created, it needs to be built
```sh
cd ~/catkin_ws
catkin build
```

This creates build, devel, and logs folders in your directory


- Now to make your workspace visible to ROS Source the setup file in the devel directory.
```sh
source ~/catkin_ws/devel/setup.bash
```

This command must be executed once for the commands like rosrun and roscd to work

- This setup.bash file needs to be sourced everytime when you want to use the ROS package inside the workspace you created.
To save typing, add this to your .bashrc,
```sh
gedit ~/.bashrc
Add to the end: source ~/catkin_ws/devel/setup.bash
```
Save and close the editor.
- If your workspace name is different then the code is a follow
```sh
source ~/<workspace_name>/devel/setup.bash
```

