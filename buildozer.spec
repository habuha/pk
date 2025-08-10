[app]
title = 趣味小游戏
package.name = funapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

requirements = python3,kivy==2.2.1,cython==0.29.33

orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.arch = armeabi-v7a,arm64-v8a

android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.private_storage = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
