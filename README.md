
In the example, you will learn how to use Keras to fine tune a MobileNet pre-train model with three easy steps

Step 1 : Data collection

Step 2 : Put data in the right folder structure

Step 3 : Edit config.json and train model with a single command


Prerequisite : install environment

install Brew    https://brew.sh/
$ ruby ​​-e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install) " 
Add the last line of ~/.profile file to export PATH=/usr/local/bin:/usr/local/sbin:$PATH to

install Python
Brew install python to

install Virtual Environment and Tensorflow  https://www. Tensorflow.org/install/install_mac 
$ sudo easy_install pip # Install pip manager
$ pip install --upgrade virtualenv # If you get an error, you need to install nose and tornado
$ pip install nose  
$ pip install tornado
$ virtualenv --system-site-packages ./tensorflow # for Python 2.7
$ virtualenv --system-site-packages -p python3 ./tensorflow          # for Python 3.n
$ cd tensorflow 
$ source ./bin/activate 
(tensorflow)$ pip install --upgrade tensorflow		         # for Python 2.7
(tensorflow)$ pip3 install --upgrade tensorflow		         #	for Python 3.nInstall

Keras    https://keras.io/#installation 
$keras Pip install

Tools to save Keras model saved to disk
$ brew install hdf5 
$ pip install h5py                             		


Install Pillow
$ pip install pillow    

Install XCode 
to the web to download and install XCode   https://developer.apple.com/xcode/ Or App-Store download
$ sudo xcode-select --install
$ sudo xcodebuild -license # Swipe to the bottom and accept the terms 

install OPENCV  https://www.learnopencv.com/install-opencv3-on-macos/
$ brew Install opencv

if there is a permission problem  e.g. brow link isl, brew link gcc, brew link hdf5
$ sudo chown -R myaccount: admin /usr/local/bin        e.g. sudo chown -R eddieliu: admin/usr/local/bin
$ sudo chown -R myaccount: admin /usr/local/share    e.g. sudo chown -R eddieliu: admin/usr/local/share


Steps 1 : Data collection

(to be continued)



