# Импортирование необходимых библиотек.
import pandas as pd
import random
import hashlib
import math

# Функция для генерации хэша имени.
def Hush(name):
    hush = int(hashlib.sha1(name.encode("utf-8")).hexdigest(), 16) % (10 ** 8)
    return hush

# 3. Уровень опасности, угрожающей студенту.
def Danger(name, VolanDeMort):
    danger = (math.ceil(abs(VolanDeMort-Hush(name)) % 50))

    return danger

# 4. Уровень владения волшебством 
# (измеряется в количестве выученных заклинаний, рецептов зелий)
def Magic(stick):
    magic = random.randint(1,3) * stick

    return magic

# 5. Количество замечаний от профессоров.
def Remark(name, prof):
    if name == 'Harry' and prof == 'Snape':
        remark =  math.ceil(4*Hush(prof) % 30)
    
    elif prof == 'Dumbledore':
        remark = 0
    
    else:
        remark = math.ceil(abs(Hush(name)-Hush(prof)) % 30)

    return remark

# 6. Количество очков, заработанных за день.
def Score(beans):
    if beans % 2 == 0:
        score = math.ceil(beans/2)
    
    else:
        score = (beans)

    return score

# 7. Количество пропущенных занятий.
def Miss(name, remarks):
    if name == 'Hermiona':
        miss = 0
    
    else:
        miss = math.ceil(remarks+Hush(name) % 30)

    return miss

# 8. Коэффициент Люпина, который придумал профессор Люпин
#  для оценки эффективности работы студентов, зависящий от пропущенных занятий,
#  уровня владения волшебством, заработанных очков и уровня опасности.
def LupCof(scores, remarks, magic, danger):
    lupin = float('{:.2f}'.format(((scores) * math.log(magic)) * (danger + remarks) / 100))

    return lupin

# 9. Количество тренировок в квидич.
def Quidditch(name, miss):
    if name == 'Hermiona' or name == 'Crabbe' or name == 'Goyle':
        quidditch = miss * 0
    
    else:
        quidditch =  math.ceil(abs(miss - Hush(name) % 50))

    return quidditch

# 10. Вероятность получения травмы, заболеть.
def Disease(danger, quidditch, VolanDeMort):
    disease = float('{:.2f}'.format(abs(VolanDeMort + danger + quidditch) / 100))

    return disease

# 11. Количество бобов у студентов.
def Beans(name):
    beans = math.ceil(math.log(math.ceil(Hush(name) % 50)))

    return beans

# 12. Функция для генерации уровня волшебной палочки студента.
def StickLevel():
    stick = random.randint(1,4)

    return stick

# 13. Деятельность Волан-Де-Морта.
def VolanDeMort():
    VolanDeMort = random.randint(1,10)

    return VolanDeMort

# Функция для заполнения датасета.
def give_dataset():
    rows = []
    names = ['Harry', 'Ron', 'Hermiona', 'Fred', 'George', 'Ginny', 'Sedric', 'Draco', 'Crabbe', 'Goyle']
    profs = ['Snape', 'Hagrid', 'Lupin', 'Trelawney', 'Mcgonagall', 'Sprout', 'Dumbledore']

    # Создание ряда датасета.
    for i in range(1,10000):
        random_name = names[random.randint(0,len(names)-1)]
        teacher = profs[random.randint(0,len(profs)-1)]
        stick = StickLevel()
        vold = VolanDeMort()

        rows.append([
        random_name, 
        Danger(random_name, vold),
        Magic(stick), 
        Remark(random_name, teacher),
        Score(Beans(random_name)),
        Miss(random_name, Remark(random_name, teacher)), 
        LupCof(Score(Beans(random_name)), Remark(random_name, teacher), Magic(stick), Danger(random_name, vold)), 
        Quidditch(random_name, Miss(random_name, Remark(random_name, teacher))), 
        Disease(Danger(random_name, vold), Quidditch(random_name, Miss(random_name, Remark(random_name, teacher))), vold), 
        Beans(random_name),
        teacher,
        stick,
        vold])
        

    df = pd.DataFrame(rows, columns=["Name", "Danger", "Magician level", "Remarks", "Scores", "Absenses",
     "Lupin coef", "Quidditch", "Disease", "Beans", "Teacher", "StickLevel", "Volan-De-Mort"])

    return df

# Главная функция.
def main():
    df = give_dataset()

    # Сохранение датасета в CSV-файл.
    df.to_csv (r'C:\Users\romav\НИР\dataset.csv', index = False, header=True)

main()

#names = ['Harry', 'Ron', 'Hermiona', 'Fred', 'George', 'Ginny', 'Sedric', 'Draco', 'Crabbe', 'Goyle']
#profs = ['Snape', 'Hagrid', 'Lupin', 'Trelawney', 'Mcgonagall', 'Sprout', 'Dumbledore']
#for i in range(len(names)):
#   print(Remark(names[i], profs[1]))