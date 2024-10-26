class employee:   #музыкальное произведение
    def __init__(self, ID: int, surname: str, salary: int, IDu: int):
        self.ID = ID
        self.surname = surname #название композиции
        self.salary = salary   #продолжительность произведения в секундах
        self.IDu = IDu

class unit:       #оркестр
    def __init__(self, ID: int, name: str):
        self.ID = ID
        self.name = name

class empUn:
    def __init__(self, mIDe: int, mIDu: int):
        self.mIDe = mIDe
        self.mIDu = mIDu

orchestra = [
    unit(1, "Симфонический оркестр Мариинского театра"),
    unit(2, "Государственный академический симфонический оркестр России имени Е. Ф. Светланова"),
    unit(3, "Московский государственный академический симфонический оркестр"),
    unit(4, "Российский государственный академический камерный «Вивальди-оркестр»"),
    unit(5, "Симфонический оркестр Государственной филармонии Республики Адыгея")
]

music = [
    employee(1, "К Элизе", 164, 1),
    employee(2, "Лунная соната", 307, 1),
    employee(3, "Пришла весна", 200, 2),
    employee(4, "Турецкий марш", 208, 2),
    employee(5, "Лунный свет", 320, 3),
    employee(6, "Шторм", 171, 3),
    employee(7, "Маленькая ночная серенада", 313, 4),
    employee(8, "Этюд № 12", 146, 4),
    employee(9, "Летняя гроза", 167, 4),
    employee(10, "Утренняя молитва", 111, 5),
    employee(11, "Я взываю к Тебе, Господи", 139, 5),
    employee(12, "Спящие пьяные", 227, 5)
]

# 1:М
mnms = [
    empUn(1, 1),
    empUn(1, 3),
    empUn(1, 5),
    empUn(2, 1),
    empUn(2, 2),
    empUn(3, 2),
    empUn(3, 5),
    empUn(3, 4),
    empUn(3, 3),
    empUn(4, 2),
    empUn(5, 3),
    empUn(6, 3),
    empUn(7, 4),
    empUn(8, 4),
    empUn(8, 1),
    empUn(9, 4),
    empUn(9, 5),
    empUn(10, 5),
    empUn(10, 2),
    empUn(10, 1),
    empUn(11, 5),
    empUn(12, 5)
]

def main():
    one_to_many:list = [(o.name, m.surname, m.salary)
                        for m in music
                        for o in orchestra
                        if m.IDu == o.ID]
    many_to_many_temp:list = [(o.name, mo.mIDu, mo.mIDe)
                                for o in orchestra
                                for mo in mnms
                                if o.ID == mo.mIDu]
    many_to_many:list = [(m.surname, m.salary, oname)
                        for oname, oID, mID in many_to_many_temp
                        for m in music if m.ID == mID]
    
    # запрос1 (связь 1:М): вывести все оркестры, у которых в названии есть "оркестр", список исп музыки
    def E1(one_to_many: list):
        l = list(sorted(filter(lambda x: "оркестр" in x[0], one_to_many)))
        return list(sorted(l))
    
    # запрос2 (связь 1:М): Выведите список оркестров со средней продолж композиции в каждом оркестре, отсортированный по средней продолж.округление до 2 знака после запятой
    def E2(one_to_many: list):
        l = sorted(one_to_many)
        res = []
        tempp = "iii"
        sr = 0
        sum = 0
        n = 0
        for g, i, f in l:
            if g != tempp:
                if n != 0:
                    sr = sum/n
                    res.append([round(sr, 2), tempp])
                tempp = g
                sr = 0
                sum = 0
                n = 0
            sum += f
            n += 1
        sr = sum/n
        res.append([round(sr, 2), tempp])   
        return sorted(res)
    
    # запрос3 (связь М:М): Выведите список всех композиций, у которых название начинается с буквы «Л», и названия их оркестров. 
    def E3(many_to_many: list):
        return list(sorted(filter(lambda x: x[0][0] == "Л", many_to_many)))
    
    print("Запрос 1\n")
    temp = "rrr"
    for  g, i, f in E1(one_to_many):
        if g != temp:
            temp = g
            print(g, ":")
        print(" -", i, ",", f, "секунд")
    
    print("\nЗапрос 2\n")
    for g, i in E2(one_to_many):
        print(i, ":", g, "секунд")

    print("\nЗапрос 3\n")
    temp = "rrr"
    for  g, i, f in E3(many_to_many):
        if g != temp:
            temp = g
            print(g, ",", i,"секунд:")
        print(" -", f)

if __name__ == '__main__':
    main()