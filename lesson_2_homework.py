"""
DƏRS 2 — EV TAPŞIRIĞI
Mövzu: Variables, Data Types, Operators və Expressions

Qaydalar:
1. Bütün tapşırıqları bu faylın içində həll edin.
2. Tapşırıqları ardıcıllıqla edin.
3. Variable adlarını mənalı yazmağa çalışın.
4. Kodunuzu hər tapşırıqdan sonra Run edib nəticəni yoxlayın.
5. Səhv (error) çıxsa, əvvəlcə error mesajına və yazdığınız sətrə diqqətlə baxın.
6. Hazır cavabı axtarmaq əvəzinə əvvəl özünüz həll etməyə çalışın.

Uğurlar :)
"""


# ============================================================
# TAPŞIRIQ 1 — Variables və Data Types
# ============================================================

# Özünüz haqqında aşağıdakı məlumatları ayrı variable-larda saxlayın:
# - ad
# - yaş
# - boy (məsələn: 1.78)
# - tələbə olub-olmamağınız (True və ya False)
#
# Sonra bütün variable-ları print() ilə ekrana çıxarın.
# Hər variable-ın Data Type-ını type() ilə ayrıca göstərin.
#
# İPUCU:
# Text üçün -> str
# Tam ədəd üçün -> int
# Onluq ədəd üçün -> float
# True / False üçün -> bool
#
# Nümunə variable adı:
# first_name
# Amma öz məlumatlarınızı və öz variable adlarınızı istifadə edin.


# Kodunuzu aşağıda yazın:
# name = "Nijat"
# age = 24
# height = 1.80
# isStudent = False
# print(type(name))
# print(name)
# print(age)
# print(type(age))
# print(height)
# print(type(height))
# print(isStudent)
# print(type(isStudent))

# ============================================================
# TAPŞIRIQ 2 — Type Conversion və input()
# ============================================================

# İstifadəçidən aşağıdakı məlumatları input() ilə alın:
# - ad
# - yaş
# - boy
#
# Yaş variable-ı int olmalıdır.
# Boy variable-ı float olmalıdır.
#
# Sonra məlumatları və onların Data Type-larını print() edin.
#
# İPUCU:
# input() ilə gələn məlumat default olaraq str olur.
#
# Lazım ola bilər:
# int(...)
# float(...)
#
# Məsələn:
# age = int(input("..."))


# Kodunuzu aşağıda yazın:
# name1=input("Enter your name: ")
# age=int(input("Enter the age: "))
# heig = float(input("Enter your height: "))
# print(name1)
# print(type(name1))
# print(age)
# print(type(age))
# print(heig)
# print(type(heig))


# ============================================================
# TAPŞIRIQ 3 — Sadə Calculator
# ============================================================

# İstifadəçidən iki ədəd alın.
#
# Bu iki ədəd üçün aşağıdakı nəticələri hesablayın:
# - cəm
# - fərq
# - vurma
# - bölmə
# - tam bölmə
# - bölmədən qalan qalıq
# - birinci ədədin ikinci ədəd qüvvəti
#
# Hər nəticəni ayrıca, aydın şəkildə print() edin.
#
# İPUCU:
# Arithmetic Operators:
# +   toplama
# -   çıxma
# *   vurma
# /   bölmə
# //  tam bölmə
# %   qalıq
# **  qüvvət
#
# Ədədləri float və ya int olaraq almağı özünüz seçə bilərsiniz.
#
# QEYD:
# İkinci ədəd üçün 0 daxil etməyin, çünki 0-a bölmək mümkün deyil.
# Error Handling-i sonrakı dərslərdə öyrənəcəyik.


# Kodunuzu aşağıda yazın:
# req1 = int(input("Ilk reqemi daxil edin: "))
# req2 = int(input("Ikinci reqemi daxil edin: "))
# sum = req1+req2
# diff = req1-req2
# mult = req1 * req2
# div = req1/req2
# full_div = req1//req2
# remainer = req1%req2
# power = req1**req2
# print("Toplam: ",sum)
# print("çıxma: ",diff)
# print("Vurma: ", mult)
# print("bölmə:", div)
# print("tam bölmə: ",full_div)
# print("Qalıq:",remainer)
# print("Qüvvət: ",power)

# ============================================================
# TAPŞIRIQ 4 — Məhsulun ümumi qiyməti
# ============================================================

# Kiçik alış-veriş proqramı yazın.
#
# İstifadəçidən alın:
# - məhsulun adı
# - bir ədəd məhsulun qiyməti
# - neçə ədəd almaq istədiyi
#
# Sonra ümumi qiyməti hesablayın:
#
# total_price = price * quantity
#
# Ekranda aşağıdakı məlumatları göstərin:
# - məhsulun adı
# - bir ədədinin qiyməti
# - miqdarı
# - ümumi qiymət
#
# İPUCU:
# Məhsulun adı -> str
# Qiymət -> float
# Miqdar -> int


# Kodunuzu aşağıda yazın:
# product_name = input("Mehsulun adini qeyd edin:")
# price = float(input("Qiymetini daxil edin: "))
# quantity = int(input("miqdari deyin: "))
# total_price = price*quantity
# print("Məhsulun adı: ",product_name)
# print("bir ədədinin qiyməti: ",price)
# print("miqdar: ",quantity)
# print("ümumi qiymət: ",total_price)



# ============================================================
# TAPŞIRIQ 5 — Comparison Operators
# ============================================================

# İstifadəçidən yaşını alın.
#
# Aşağıdakı müqayisələrin nəticəsini ayrı variable-larda saxlayın:
#
# 1. Yaş 18-ə böyük və ya bərabərdir?
# 2. Yaş 30-dan kiçikdir?
# 3. Yaş tam olaraq 25-dir?
# 4. Yaş 18-ə bərabər deyil?
#
# Sonra bütün nəticələri print() edin.
#
# Nəticələrin True və ya False olmasına diqqət edin.
#
# İPUCU:
# ==  bərabərdir?
# !=  bərabər deyil?
# >   böyükdür?
# <   kiçikdir?
# >=  böyük və ya bərabərdir?
# <=  kiçik və ya bərabərdir?


# Kodunuzu aşağıda yazın:
# age = int(input("Yaşınızı qeyd edin:"))
# print(age>=18)
# print(age<30)
# print(age==25)
# print(age!=18)



# ============================================================
# TAPŞIRIQ 6 — Logical Operators
# ============================================================

# Aşağıdakı variable-ları yaradın:
#
# age = istifadəçidən alınsın
# has_ticket = True
# is_banned = False
#
# Sonra aşağıdakı sualların cavabını expression-larla hesablayın:
#
# 1. İstifadəçi 18 və ya daha böyükdür VƏ bileti var?
# 2. İstifadəçinin bileti var VƏ qadağan olunmayıb?
# 3. İstifadəçi 18-dən kiçikdir VƏ YA qadağan olunub?
#
# Nəticələri ayrı variable-larda saxlayın və print() edin.
#
# İPUCU:
# and -> hər iki tərəf True olmalıdır
# or  -> tərəflərdən ən az biri True olmalıdır
# not -> True/False dəyərini tərsinə çevirir
#
# Məsələn:
# result = age >= 18 and has_ticket
#
# Conditional Statements (if/else) istifadə etməyin.
# Onu növbəti dərsdə öyrənəcəyik.


# Kodunuzu aşağıda yazın:
# age = int(input("Yaşınızı qeyd edin:"))
# has_ticket = True
# is_banned = False
# print(age>=18 or has_ticket)
# print(has_ticket and is_banned)
# print(age<18 or not is_banned)


# ============================================================
# TAPŞIRIQ 7 — Assignment Operators
# ============================================================

# balance adlı variable yaradın və başlanğıc dəyərini 200 edin.
#
# Sonra yalnız Assignment Operators istifadə edərək:
#
# 1. Balansa 100 əlavə edin.
# 2. Balansdan 50 çıxın.
# 3. Balansı 2-yə vurun.
# 4. Balansı 5-ə bölün.
#
# Hər əməliyyatdan sonra balance variable-ını print() edin.
#
# İPUCU:
# +=
# -=
# *=
# /=
#
# Məsələn:
# balance += 100


# Kodunuzu aşağıda yazın:
# balance=200
# balance+=100
# print(balance)
# balance-=50
# print(balance)
# balance*=2
# print(balance)
# balance/=5
# print(balance)



# ============================================================
# TAPŞIRIQ 8 — Operator Precedence
# ============================================================

# Aşağıdakı iki expression-ın nəticəsini əvvəlcə kodu Run etmədən
# özünüz təxmin edin.
#
# Sonra Python ilə hesablayıb cavabınızı yoxlayın.
#
# Expression 1:
# 10 + 5 * 2
#
# Expression 2:
# (10 + 5) * 2
#
# Hər nəticəni ayrı variable-da saxlayın və print() edin.
#
# Sonra comment olaraq yazın:
# Niyə bu iki nəticə fərqli oldu?
#
# İPUCU:
# Python-da vurma (*) toplamadan (+) əvvəl hesablanır.
# Mötərizə () isə əməliyyatların sırasını dəyişmək üçün istifadə edilə bilər.


# Kodunuzu aşağıda yazın:
a=10 + 5 * 2
b=(10 + 5) * 2
print(a)
print(b)
#Burda moterizeye gore de netice ferqli oldu əməliyyatların sırasını dəyişdiyine gore


# ============================================================
# TAPŞIRIQ 9 — FINAL TASK: Aylıq büdcə proqramı
# ============================================================

# İndi dərsdə öyrəndiyimiz mövzuları bir tapşırıqda birləşdirin.
#
# İstifadəçidən aşağıdakı məlumatları alın:
# - ad
# - aylıq gəlir
# - aylıq kirayə xərci
# - aylıq yemək xərci
# - digər aylıq xərclər
#
# Sonra hesablayın:
#
# 1. Ümumi aylıq xərc
# 2. Ayın sonunda qalan pul
# 3. İllik gəlir (aylıq gəlir * 12)
# 4. Ayın sonunda pul qalıb-qalmadığını True/False olaraq
# 5. Ümumi aylıq xərcin gəlirdən böyük olub-olmadığını True/False olaraq
#
# Sonda məlumatları aydın şəkildə print() edin.
#
# Məsələn output-un görünüşü təxminən belə ola bilər:
#
# Ad: Ali
# Aylıq gəlir: 1500.0
# Ümumi xərc: 1000.0
# Qalan pul: 500.0
# İllik gəlir: 18000.0
# Pul qalır: True
# Xərclər gəlirdən çoxdur: False
#
# Rəqəmləri özünüz daxil edəcəksiniz.
#
# İPUCU 1:
# total_expenses = ...
#
# İPUCU 2:
# remaining_money = monthly_income - total_expenses
#
# İPUCU 3:
# yearly_income = monthly_income * 12
#
# İPUCU 4:
# Comparison expression nəticəsi birbaşa bool olur:
# remaining_money > 0
#
# İPUCU 5:
# Bu tapşırıqda if/else lazım deyil.
#
# Məqsəd:
# Variables + Data Types + input() + Type Conversion +
# Arithmetic Operators + Comparison Operators + Expressions
# mövzularını birlikdə işlətməkdir.


# Kodunuzu aşağıda yazın:
name = input("Adiniz nedir?: ")
monthly_income = float(input("Ayliq geliriniz: "))
monthly_rental_expenses = float(input("aylıq kirayə xssərciniz: "))
monthly_food_expenses = float(input("aylıq yemək xərciniz: "))
other_monthly_expenses = float(input("Ayliq diger xercleriniz: "))
total_monthly_expense = monthly_rental_expenses+monthly_food_expenses+other_monthly_expenses
remaining_money = monthly_income - total_monthly_expense
yearly_income = monthly_income*12
print(remaining_money>0)
print("Xərclər gəlirdən çoxdur: ",total_monthly_expense>monthly_income)                         

