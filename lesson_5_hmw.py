"""
Dərs 5 — Ev tapşırığı
Mövzular:
- Conditional Statements və Loops — əlavə mövzular
- Strings ilə işləmə

Qaydalar:
- Bütün tapşırıqları bu faylın içində həll edin.
- Tapşırıq şərhlərini silməyin.
- Hər tapşırığın kodunu uyğun hissənin altına yazın.
- Proqramı fərqli input-larla test edin.
- Hazır kodu internetdən copy-paste etməyin.
- Məqsəd syntax-ı əzbərləmək yox, məntiqi özünüz qurmaqdır.
"""

# ============================================================
# TAPŞIRIQ 1 — Username yoxlanışı
# ============================================================

# İstifadəçidən username alın.
# Qaydalar:
# - əvvəl və sondakı boşluqlar silinsin
# - minimum 5 character olsun
# - username daxilində space olmasın
#
# Uyğundursa:
# Username accepted
#
# İPUCU:
# strip(), len(), " " in username, if / elif / else

# Kodunuzu burada yazın:
username = input("Username:").strip()
if len(username)>4 and " " not in username:
    print("Username accepted")
elif len(username)<5:
    print("minimum 5 character olsun!")
else:
    print("Username is not accepted")

# ============================================================
# TAPŞIRIQ 2 — Mətn analizi
# ============================================================

# İstifadəçidən bir text alın.
# Çap edin:
# - ümumi uzunluq
# - ilk character
# - son character
# - böyük hərflərlə forması
# - kiçik hərflərlə forması
#
# İPUCU:
# len(), indexing, negative indexing, upper(), lower()

# Kodunuzu burada yazın:
text=input("Texti daxil edin:")
print(len(text))
print(text[0])
print(text[-1])
print(text.upper())
print(text.lower())

# ============================================================
# TAPŞIRIQ 3 — Sözün tərsinə çevrilməsi
# ============================================================

# İstifadəçidən bir söz alın və tərsinə çevirib çap edin.
#
# Nümunə:
# Python -> nohtyP
#
# İPUCU:
# slicing və mənfi step istifadə edin.

# Kodunuzu burada yazın:
word=input("Sozunu daxil edin:")
print(word[::-1])

# ============================================================
# TAPŞIRIQ 4 — Character sayı
# ============================================================

# İstifadəçidən bir söz və ayrıca bir character alın.
# Həmin character-in söz daxilində neçə dəfə olduğunu hesablayın.
# Böyük və kiçik hərf fərqi nəzərə alınmasın.
#
# İPUCU:
# lower(), for loop, if
# count = 0

# Kodunuzu burada yazın:
word=input("Enter word:").lower()
character= input("Enter character:").lower()
print(word.count(character))

# ============================================================
# TAPŞIRIQ 5 — Fayl növünü müəyyən edin
# ============================================================

# İstifadəçidən file name alın.
#
# .py   -> Python file
# .txt  -> Text file
# .jpg  -> Image file
# .png  -> Image file
# digər -> Unknown file type
#
# İPUCU:
# endswith(), if / elif / else, or

# Kodunuzu burada yazın:
filename=input("Faylin adini daxil edin:")
if filename.endswith(".py"):
    print("Python file")
elif filename.endswith(".txt"):
    print("Text file")
elif filename.endswith(".jpg") or filename.endswith(".png"):
    print("Image file")
else:
    print("Unknown file type")
# ============================================================
# TAPŞIRIQ 6 — Command sistemi
# ============================================================

# İstifadəçidən command alın.
#
# start   -> Starting...
# stop    -> Stopping...
# restart -> Restarting...
# status  -> System is running
# digər   -> Unknown command
#
# Böyük və kiçik hərf fərqi nəzərə alınmasın.
#
# İPUCU:
# input(...).strip().lower()
# match / case istifadə edin.

# Kodunuzu burada yazın:
command=input("Emrini qeyd edin:").strip().lower()
match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "restart":
        print("Restarting...")
    case "status":
        print("System is running")
    case _:
        print("Unknown command")
# ============================================================
# TAPŞIRIQ 7 — Password yoxlanışı
# ============================================================

# İstifadəçidən password alın.
#
# Qaydalar:
# - minimum 8 character
# - space olmamalidir
# - daxilində ən azı bir rəqəm olmalıdır
#
# Uyğundursa:
# Strong password
#
# Əks halda:
# Weak password
#
# QEYD:
# Hazır digit-checking method keçməmisiniz.
# Rəqəmləri String kimi yoxlaya bilərsiniz:
# "0", "1", ..., "9"
#
# İPUCU:
# has_digit = False
# for char in password:
#     ...
# Rəqəm tapsanız has_digit = True edin.

# Kodunuzu burada yazın:
password=input("Enter your password: ")
has_digit = False
for char in password:
    if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        has_digit = True
        break
if len(password)>=8 and " " not in password and has_digit:
    print("Strong password")
else:
    print("Weak password")
# ============================================================
# TAPŞIRIQ 8 — Palindrome yoxlanışı
# ============================================================

# İstifadəçidən bir söz alın.
#
# Tərsinə oxunduqda da eynidirsə:
# Palindrome
#
# Əks halda:
# Not palindrome
#
# Böyük və kiçik hərf fərqi nəzərə alınmasın.
#
# İPUCU:
# lower(), slicing

# Kodunuzu burada yazın:
word=input("bir söz daxil edin:").lower()
if word==word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
# ============================================================
# YEKUN TAPŞIRIQ — Sadə giriş sistemi
# ============================================================

# Bu məlumatlardan istifadə edin:
#
# correct_username = "admin"
# correct_password = "python123"
#
# İstifadəçiyə maksimum 3 cəhd verin.
#
# Hər cəhddə username və password daxil etsin.
#
# Username üçün:
# - əvvəl və sondakı boşluqları silin
# - böyük və kiçik hərf fərqi nəzərə alınmasın
#
# Əgər məlumatlar doğrudursa:
# Login successful
# çap edin və loop dayansın.
#
# Səhvdirsə:
# Invalid username or password
# çap edin.
#
# 3 cəhd bitdikdən sonra login alınmayıbsa:
# Too many failed attempts
# çap edin.
#
# İPUCU:
# for + range()
# if
# break
# loop else
# strip()
# lower()

# Kodunuzu burada yazın:
correct_username = "admin"
correct_password = "python123"
for i in range(3):
    username=input("Isdifadechi adini qeyd edin:").strip().lower()
    password=input("Shifreni qeyd edin")
    if username==correct_username and password==correct_password:
        print("Login successful")
        break
    else:
        print("Invalid username or password")
else:
    print("Too many failed attempts. Try again in 5 minutes!")