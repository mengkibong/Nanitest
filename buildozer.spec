[app]
# Nama app
title = ExcelApp
package.name = excelapp
package.domain = org.example
source.dir = .
source.include_exts = py,csv,kv,xlsx

# Requirements Python + Kivy
requirements = python3,kivy

# Versi app
version = 1.0.0

# Minimum dan target Android API
android.minapi = 21
android.api = 33
android.arch = armeabi-v7a

# Ikon & splash screen (optional)
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

# Permissions untuk baca/tulis fail di Android
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Log level
log_level = 2
