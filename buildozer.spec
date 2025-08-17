[app]
# Nama app
title = ExcelApp
package.name = excelapp
package.domain = org.example

# Script utama
source.include_exts = py,csv,kv,xlsx
source.dir = .

# Requirements
requirements = python3,kivy

# Versi android minimum
android.minapi = 21

# Versi android target
android.api = 33
android.arch = armeabi-v7a

# Ikon & splash screen (optional)
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

# Permissions (jika perlukan baca/tulis file)
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Buildozer log level
log_level = 2