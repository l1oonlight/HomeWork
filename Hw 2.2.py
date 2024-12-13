#Условия : округлить до сотых
waste = int(input())
if waste > 20:
    print(f'Итоговая стоимость равна : {round(waste - (waste * 0.35), 2)} \nСкидка равна : 35%')
else:
    print(f'Итоговая стоимость равна : {waste} \nСкидка равна : Error: The discount was not detected')