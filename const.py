'''
КОНСТАНТЫ
VOTEBAN BOT
'''

# Constants
nokick = {'sasha_pankratiew', 'alexey_shilo', 'id136385345', 'id138738887', '138738887', '136385345'}

file_name = 'v.ban'

vote_count = 5 # Минимальное кол-во голосов
vote_time = 2 # Количество минут, сколько длится голосование
spam_time = 10.0 # Анти-спам задержка (в секундах)
friends_time = 60.0 # Интервал (в минутах) проверки друзей
backups_time = 5 # Интервал проведения бэкапа списка заблокированных


anti_kick_commands = {'!нет','!-','!no','!некик','!некикаемнахой'} # Команды для кика
kick_commands = {'!да', '!yes', '!+', 'кик','!кикаемнахой'} # Команды против кика
