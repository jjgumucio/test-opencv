# Dependencies
apt-get update && apt-get install -y 
    cmake 
    gfortran \
    libatlas-base-dev \
    python \
    python-dev \
    wget

# pip
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py && rm get-pip.py

# Python stack
pip install numpy

# Download OpenCV and extra modules
git clone https://github.com/Itseez/opencv.git
cd opencv
git checkout tags/3.1.0

cd ..
git clone https://github.com/Itseez/opencv_contrib.git
cd opencv_contrib
git checkout tags/3.1.0
cd ..

# Build OpenCV
cd opencv
cmake -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules . && \
    make && make install && \
    ldconfig && \
    cd .. && \
    rm -rf opencv && \
    rm -rf opencv_contrib