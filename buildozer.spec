[app]
# Maklumat app
title = ExcelApp
package.name = excelapp
package.domain = org.nani
source.dir = .
version = 0.1
requirements = python3,kivy,pandas,openpyxl
icon.filename = icon.png   # optional, letak icon kalau ada

[buildozer]
log_level = 2
warn_on_root = 1

[android]
# Tetapan Android
android.archs = arm64-v8a, armeabi-v7a
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.entrypoint = org.kivy.android.PythonActivity
android.permissions = INTERNET
