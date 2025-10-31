from django.db import models


# ===============================
# 🏠 موديل الصفحة الرئيسية (Home)
# ===============================
class Home(models.Model):
    name = models.CharField(max_length=20)
    greetings_1 = models.CharField(max_length=5)
    greetings_2 = models.CharField(max_length=5)
    picture = models.ImageField(upload_to='picture/')
    update = models.DateTimeField(auto_now=True)  # آخر تحديث تلقائيًا

    def __str__(self):
        return self.name


# ===============================
# 👤 موديل صفحة "عنّي" (About)
# ===============================
class About(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField()
    career = models.CharField(max_length=200)
    
    profile = models.ImageField(upload_to='about/', blank=True, null=True)
    update = models.DateTimeField(auto_now=True)  # أضفنا الحقل لتتبع آخر تحديث

    def __str__(self):
        return self.heading


# ===============================
# 🌐 موديل روابط التواصل الاجتماعي (Profile)
# ===============================
class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='profiles')
    social_name = models.CharField(max_length=50)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.social_name


# ===============================
# 🧩 موديل تصنيفات المهارات (Category)
# ===============================
class Category(models.Model):
    name = models.CharField(max_length=50)
    update = models.DateTimeField(auto_now=True)  # تم تغييره من DateField إلى DateTimeField

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name


# ===============================
# 💪 موديل المهارات (Skills)
# ===============================
class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=50)

    def __str__(self):
        return self.skill_name


# ===============================
# 🖼️ موديل المشاريع أو الأعمال (Portfolio)
# ===============================
class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Portfolio {self.id}'



class Message(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"