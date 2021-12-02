from bank import Bank
from person import Legal_person, Physique_person
from count import Savings_account, Checking_account, Legal_account

from os import system

information = []
banks = []

def add_bank(bank):
    global banks
    times = 0

    banks.append({"Bank": bank.name, "bank_actions": bank})

    for i in banks:
        if i["Bank"] == bank.name:
            times += 1
        if times > 1:
            banks.pop()

def create_client(client, count, bank):
    global information

    client.count = count

    person = {"Client": client.name, "Count_actions": count, "Client_actions": client}
    information.append(person)

    add_bank(bank)

def modify_count(client, count):
    for i in banks:
        if i["bank_actions"].autenticate(client.name, count.agency, count.count):
            if isinstance(count, Checking_account):
                print("Vamos trocar para uma conta poupança: ")
                agency = input("Digite a nova agência: ").strip()
                count_number = input("Digite a nova conta: ").strip()
                balance = float(input("Digite o novo saldo: ").strip())
                new_count = Savings_account(agency, count_number, balance)
                i["bank_actions"].update_client(client.name, new_count)

                client.count = new_count

                count.agency = agency
                count.count = count
                count.balance = balance

                for j in information:
                    if j["Client"] == client.name:
                        j["Count_actions"] = new_count

                break
            
            elif isinstance(count, Savings_account):
                print("Vamos trocar para uma conta corrente: ")
                agency = input("Digite a nova agência: ").strip()
                count_number = input("Digite a nova conta: ").strip()
                balance = input("Digite o novo saldo: ").strip()
                limit = float(input("Digite o novo limite: ").strip())
                new_count = Checking_account(agency, count_number, balance, limit)
                i["bank_actions"].update_client(client.name, new_count)

                client.count = new_count

                count.agency = agency
                count.count = count
                count.balance = balance
                count.limit = limit

                for j in information:
                    if j["Client"] == client.name:
                        j["Count_actions"] = new_count

                break
            
            elif isinstance(count, Legal_account):
                print("Vamos criar uma nova conta jurídica: ")
                agency = input("Digite a nova agência: ").strip()
                count = input("Digite a nova conta: ").strip()
                balance = input("Digite o novo saldo: ").strip()
                limit = float(input("Digite o novo limite: ").strip())
                new_count = Legal_account(agency, count, balance, limit)
                i["bank_actions"].update_client(client.name, new_count)

                client.count = new_count

                count.agency = agency
                count.count = count
                count.balance = balance
                count.limit = limit

                for j in information:
                    if j["Client"] == client.name:
                        j["Count_actions"] = new_count

                break

def modifyPerson(oldPerson, newPerson, personActions, count):
    for j in information:
        if j["Client"] == oldPerson:
            j["Client"] = newPerson
            j["Client_actions"] = personActions
            for i in banks:
                if i["bank_actions"].autenticate(oldPerson, count.agency, count.count):
                    i["bank_actions"].update_client(newPerson, count, oldPerson)

while True:
    system("cls")

    bank_name = input("Digite o nome do banco: ").strip().title()
    bank = Bank(bank_name)

    while True:
        choice = input("Qual tipo de funcionário deseja adicionar? Physique ou Legal: ps:Digite o nome como aparece! ").strip().lower()
        
        if choice == "physique":
            name = input("Digite seu nome: ").strip().title()
            date = input("Digite a data completa do seu aniversário: Ex:dd/mm/yyyy: ").strip()
            cpf = input("Digite seu cpf completo: ").strip()
            while True:
                choice = input("Deseja criar que tipo de conta? Checking ou Savings: ps:Digite o nome como aparece! ").strip().lower()
                if choice == "checking":
                    agency = input("Digite a agência: ").strip()
                    count = input("Digite o número da conta: ").strip()
                    balance = float(input("Digite o saldo inicial: ").strip())
                    limit = float(input("Digite o limite de crédito: ").strip())

                    count = Checking_account(agency, count, balance, limit)
                    person = Physique_person(name, date, cpf, count)

                    bank.insert_client(person, count)

                    create_client(person, count, bank)

                    break

                elif choice == "savings":
                    agency = input("Digite a agência: ").strip()
                    count = input("Digite o número da conta: ").strip()
                    balance = float(input("Digite o saldo inicial: ").strip())

                    count = Savings_account(agency, count, balance)
                    person = Physique_person(name, date, cpf, count)

                    bank.insert_client(person, count)

                    create_client(person, count, bank)

                    break
                
                else:
                    print("Opção inválida!")

        elif choice == "legal":
            name = input("Digite o nome da empresa: ").strip().title()
            date = input("Quando a empresa foi criada? Ex: dd/mm/yyyy: ").strip()
            cnpj = input("Digite o cnpj completo: ").strip()
            indentification_number = input("Digite o número de identificação completo: ").strip()
            
            print("-=-" * 20)
            print("\033[34mVocê está criando uma conta jurídica\033[m")
            print("-=-" * 20)

            agency = input("Digite a agência: ").strip()
            count = input("Digite o número da conta: ").strip()
            balance = float(input("Digite o saldo inicial: ").strip())
            limit = float(input("Digite o limite de crédito: ").strip())

            count = Legal_account(agency, count, balance, limit)
            person = Legal_person(name, date, cnpj, indentification_number, count)
            bank.insert_client(person, count)
            
            create_client(person, count, bank)
        else:
            print("Opção inválida!")

        option = input(f"Deseja inserir mais algum cliente no banco {bank.name}? S ou N: ").strip().upper()
        option = option[:1]

        if option == "N":
            break
        elif option == "S":
            continue
        else:
            print("Opção inválida!")
    
    option = input(f"Deseja inserir um novo banco e novos clientes? S ou N: ").strip().upper()
    option = option[:1]

    if option == "N":
        break
    elif option == "S":
        continue
    else:
        print("Opção inválida!")

while True:
    system("cls")
    while True:
        for i in banks:
            print(f"Clientes adicionados ao banco {i['Bank']}:")
            for client in i["bank_actions"]:
                print(f"Cliente: {client['Name']}")

        client = input("Digite o nome do cliente que deseja acessar: ").strip().title()
        Count_actions = None
        Client_actions = None
        for person in information:
            if person["Client"] == client:
                Count_actions = person["Count_actions"]
                Client_actions = person["Client_actions"]
        while True:
            if isinstance(Client_actions, Physique_person):
                choice = input("Deseja realizar ações na count ou person? ").strip().lower()
                if choice == "count":
                
                    list_actions_saving = ["Balance", "Withdraw", "Count"]
                    list_actions_checking = ["Balance", "Withdraw", "Count", "Loan"]
                    if isinstance(Count_actions, Savings_account):
                        print("Lista de ações para conta poupança: ")
                        for i in list_actions_saving:
                            print(i)

                    elif isinstance(Count_actions, Checking_account):
                        print("Lista de ações para conta corrente: ")
                        for i in list_actions_checking:
                            print(i)

                    action = input("Digite aqui a ação a ser realizada: ").strip().lower()
                    choice = input("Deseja atualizar[A] ou verificar[V] as informações? ").strip().upper()

                    if choice == "A":
                        match action:
                            case "count":
                                modify_count(Client_actions, Count_actions)
                            
                            case "balance":
                                value = float(input("Digite o valor que deseja depositar: ").strip())
                                Count_actions.deposit(value)
                                print(f'O novo saldo é de R${Count_actions.balance}')

                            case "withdraw":
                                value = float(input("Digite o valor que deseja sacar: ").strip())
                                Count_actions.withdraw(value)
                                print(f'O novo saldo é de R${Count_actions.balance}')

                            case "loan":
                                value = float(input("Digite o valor que deseja tirar de empréstimo: ").strip())
                                
                                Count_actions.loan = value

                                if Count_actions.loan > 0:
                                    print(f'Você tirou um empréstimo no valor de R${Count_actions.loan}')
                                else:
                                    print(f'Valor inválido para empréstimo')
                            
                            case _:
                                print("Opção inválida!")
                                    
                    elif choice == "V":
                        match action:
                            case "count":
                                print(Count_actions)
                            
                            case "balance":
                                print(Count_actions.balance)

                            case "withdraw":
                                print(Count_actions.balance)
                            
                            case "loan":
                                print(Count_actions.loan)
                            
                            case _:
                                print("Opção inválida!")

                elif choice == "person":
                    list_actions = ["Name", "Age", "Cpf", "Date", "Count"]
                    print("Lista de ações para a pessoa: ")
                    for i in list_actions:
                        print(i)

                    action = input("Digite aqui a ação a ser realizada: ").strip().lower()
                    choice = input("Deseja atualizar[A] ou verificar[V] as informações? ").strip().upper()

                    if choice == "A":
                        match action:
                            case "name":
                                new_name = input("Digite o novo nome: ").strip().title()
                                oldPerson = Client_actions.name
                                Client_actions.name = new_name
                                modifyPerson(oldPerson, new_name, Client_actions, Count_actions)

                            case "age":
                                new_date = input("Digite a nova data de nascimento: ex: dd/mm/yyyy:").strip()
                                Client_actions.date = new_date

                            case "cpf":
                                new_cpf = input("Digite o novo cpf").strip()
                                Client_actions.cpf = new_cpf

                            case "date":
                                new_date = input("Digite a nova data de aniversário: ex: dd/mm/yyyy: ").strip()
                                Client_actions.date = new_date

                            case "count":
                                modify_count(Client_actions, Count_actions)

                    elif choice == "V":
                        match action:
                            case "name":
                                print(f"O nome do cliente é: {Client_actions.name}")

                            case "age":
                                print(f"A idade do cliente é: {Client_actions.age()} anos")

                            case "cpf":
                                print(f"O cpf do cliente é: {Client_actions.cpf}")

                            case "date":
                                print(f"A data do aniversário do cliente é: {Client_actions.date}")

                            case "count":
                                print(f"As informações bancárias do cliente são: {Client_actions.count}")

            elif isinstance(Client_actions, Legal_person):
                choice = input("Deseja realizar ações na count ou person? ").strip().lower()
                if choice == "count":

                    list_actions = ["Balance", "Loan", "Investment", "Withdraw", "Count"]
                    
                    print("Lista de ações para conta: ")
                    for i in list_actions:
                        print(i)

                    action = input("Digite aqui a ação a ser realizada: ").strip().lower()
                    choice = input("Deseja atualizar[A] ou verificar[V] as informações? ").strip().upper()

                    if choice == "A":
                        match action:
                            case "count":
                                modify_count(Client_actions, Count_actions)
                            
                            case "balance":
                                value = float(input("Digite o valor que deseja depositar: ").strip())
                                Count_actions.deposit(value)

                            case "loan":
                                value = float(input("Digite o valor que deseja pegar de empréstimo: ").strip())
                                Count_actions.loan = value

                                if Count_actions.loan > 0:
                                    print(f'Você tirou um empréstimo no valor de R${Count_actions.loan}')
                                else:
                                    print(f'Valor inválido para empréstimo')

                            case "investment":
                                value = float(input("Digite o valor que deseja investir: ").strip())
                                Count_actions.investment = value

                            case "withdraw":
                                value = float(input("Digite o valor que deseja sacar: ").strip())
                                print(Count_actions.withdraw(value))
                            
                            case _:
                                print("Opção inválida!")
                                    
                    elif choice == "V":
                        match action:
                            case "count":
                                print(Count_actions)
                            
                            case "balance":
                                print(Count_actions.balance)

                            case "loan":
                                print(Count_actions.loan)

                            case "investment":
                                print(Count_actions.investment)

                            case "withdraw":
                                print(Count_actions.balance)
                            
                            case _:
                                print("Opção inválida!")

                elif choice == "person":
                    list_actions = ["Name", "Age", "Cnpj", "Indentification_number", "Count", "Date"]
                    print("Lista de ações para a pessoa: ")
                    for i in list_actions:
                        print(i)

                    action = input("Digite aqui a ação a ser realizada: ").strip().lower()
                    choice = input("Deseja atualizar[A] ou verificar[V] as informações? ").strip().upper()

                    if choice == "A":
                        match action:
                            case "name":
                                new_name = input("Digite o novo nome: ").strip().title()
                                oldPerson = Client_actions.name
                                Client_actions.name = new_name
                                modifyPerson(oldPerson, new_name, Client_actions, Count_actions)

                            case "age":
                                new_date = input("Digite a nova data de criação da empresa: ex: dd/mm/yyyy: ").strip()
                                Client_actions.date = new_date

                            case "cnpj":
                                new_cpf = input("Digite o novo cnpj: ").strip()
                                Client_actions.cpf = new_cpf

                            case "indentification_number":
                                new_number = input("Digite o novo número de identificação: ").strip()
                                Client_actions.indentification_number = new_number

                            case "date":
                                new_date = input("Digite a nova data de criação da empresa: ex: dd/mm/yyyy: ").strip()
                                Client_actions.date = new_date

                            case "count":
                                modify_count(Client_actions, Count_actions)

                    elif choice == "V":
                        match action:
                            case "name":
                                print(f"O nome do cliente é: {Client_actions.name}")

                            case "age":
                                print(f"A empresa existe há: {Client_actions.age()} anos")

                            case "cnpj":
                                print(f"O cnpj do cliente é: {Client_actions.cnpj}")

                            case "indentification_number":
                                print(f"O número de identificação do cliente é: {Client_actions.registration}")

                            case "date":
                                print(f"A data de criação da empresa é: {Client_actions.date}")

                            case "count":
                                print(f"As informações bancárias do cliente são: {Client_actions.count}")
                    
            choice = input(f"Deseja verificar mais alguma informação no cliente {Client_actions.name}: Sim(S) ou Não(N):").strip().lower()
            if choice == "s":
                continue
            elif choice == "n":
                break

        choice = input("Deseja acessar mais algum cliente? Sim[S] ou Não[N]: ").strip().upper()                       
        if choice == "S":
            continue
        elif choice == "N":
            break

    choice = input("Deseja validar algum cliente? Sim[s] ou Não[n]: ").strip().lower()
    if choice == "s":
        bank_action = None
        for i in banks:
            print(i["Bank"])

        bank_name = input("Digite o nome do banco para validar alguém: ").strip().title()

        for j in banks:
            if j["Bank"] == bank_name:
                person_name = input("Digite o nome do cliente: ").strip().title()
                agency_number = input("Digite o nome da agência: ").strip()
                count_number = input("Digite o número da conta: ").strip()
                functions = j["bank_actions"]
                if functions.autenticate(person_name, agency_number, count_number):
                    print(f"O cliente {person_name} é cliente do banco {bank_name}")
                else:
                    print(f"A pessoa {person_name} não é cliente do banco {bank_name}")
    else:
        print("Obrigado por utilizar nossos serviços :)")
        break
        
    choice = input("Deseja validar mais algum cliente? Sim[S] ou Não[N]: ").strip().upper()
    if choice == "S":
        continue
    elif choice == "N":
        print("Obrigado por utilizar nossos serviços :)")
        break