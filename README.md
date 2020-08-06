# raspi-camera-tutorial
Raspberry Pi 4に取り付けたカメラモジュールのチュートリアル

## 準備
1. Raspberry Pi 4にRaspbian OSをインストールする。
2. 初期設定を行い、カメラモジュールを使えるようにする。
3. このリポジトリを任意のディレクトリにクローンする。
```sh
$ cd ~/
$ git clone raspi-camera-tutorial
```
4. venvを用意する。
```sh
$ cd raspi-camera-tutorial
$ python3 -m venv venv
$ source venv/bin/activate
```
5. 必要なライブラリをインストールする。
```sh
(venv) $ pip install -r requirements.txt
```
6. OpenCVに必要なソフトウェアをインストールする
```sh
# なお、libqt4-devはheadlessの場合不要
(venv) $ apt install libhdf5-dev libhdf5-serial-dev libjasper-dev libqt4-dev libatlas-base-dev
```
7. 定義が通っていないライブラリを設定する。
```sh
(venv) $ vi ~/.bashrc
```
に以下を追記する。
```sh
export LD_PRELOAD=/usr/bin/arm-linux-gnueabihf/libatomic.so.1
```
