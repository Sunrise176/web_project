from flask import Flask, render_template, redirect, request, session
from data import db_session
from data.users import User
from data.decks import Deck
from data import binds
from forms.user import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
username = 'Гость'
user = None
is_login = False
new_deck = []
deck_is_8 = False
#if not session['username']:
#    session['username'] = username
#    session['user'] = user
#    session['is_login'] = is_login
#else:
#    session['username'] = username
pages = ['enslaved_miner', 'miner', 'crawler', 'dead', 'bomber', 'sicklewrath', 'swordwrath', 'archidon', 'eclipsor', 'shadowrath', 'spearton',
         'juggerknight', 'riprider', 'toxic_dead', 'enslaved_giant', 'giant', 'meric', 'magikill', 'illuminate', 'miner_hustle', 'rage', 'surge',
         'tesla_coil', 'acid_rain', 'heavy_healing_wisp', 'lightning_storm', 'projectile_barrier', 'snow_squall', 'healing_ward', 'scorch',
         'boyers_trap', 'brilliance', 'castle_archer', 'enchanted_pike', 'mana_burst', 'miner_upgrade', 'mining_engineer', 'monstrosity']

db_sess, db_sess_deck = None, None
def main():
    global db_sess, db_sess_deck
    binds.Base.metadata.create_all(binds.engine1)
    binds.Base.metadata.create_all(binds.engine2)
    db_sess = binds.session1
    db_sess_deck = binds.session2
    app.run()

@app.route('/')
def Main():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='Это мейн страница', log=is_login)

@app.route('/enslaved_miner')
def Enslaved_miner():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    region = request.args.get('region')
    print(f"Кликнут регион: {region}")
    return render_template('main.html', username=f'{username}', text='Легкая экономическая единица Хаотической Империи. Собирает золото и кристаллы из ресурсных узлов с каждым взмахом своей кирки.$Требование: Необходимо иметь Порабощенного шахтера или Шахтера в вашей команде.$Добыча: Размахивает киркой, чтобы добывать золото или кристаллы из ресурсных узлов.$Порабощенные шахтеры — это экономические единицы Хаоса. Как следует из названия, они могут быть захвачены у Империи Порядка.', image='enslaved_miner.png', log=is_login)

@app.route('/miner')
def Miner():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='Тяжёлая экономическая единица Империи Порядка. Собирает золото и кристаллы из ресурсных узлов с каждым взмахом кирки.$Требуется: Наличие Шахтера или Порабощенного шахтера в вашей команде.$Добыча: Размахивает киркой, чтобы извлекать золото или кристаллы из ресурсных узлов.$Шахтёрами управляет самый богатый человек Инаморты — самопровозглашённый и носящий титулы «Бог Золота», «Император Императоров» и «Крёстный Отец Величия» по имени Лэвиш.', image='miner.png', log=is_login)

@app.route('/crawler')
def Crawler():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='Очень быстрый, лёгкий ближний боец Хаотической Империи с низким здоровьем. Дешёвый, расходный юнит, эффективный в начале сражений.', image='crawler.png', log=is_login)

@app.route('/dead')
def Dead():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='Лёгкий мёртвый ближний боец Хаотической Империи с низким здоровьем. Дешёвый, расходный юнит, который быстро обучается.', image='dead.png', log=is_login)

@app.route('/bomber')
def Bomber():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='Диверсионный отряд Хаоса, вызывающий разрушительный взрыв при контакте с врагом.', image='bomber.png', log=is_login)

@app.route('/sicklewrath')
def Sicklewrath():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ОПИСАНИЕ$ Лёгкий ближний боец Империи Порядка с низким здоровьем. Наносит урон по площади с помощью серпа. Эффективен против лёгких юнитов.$ЛОР$ Серпогневы были созданы Вождём Серпведем. Изначально обычные фермеры, они превратились в грозную силу, когда Серпведь нашёл новое применение изогнутому железному лезвию.', image='sicklewrath.png', log=is_login)

@app.route('/swordwrath')
def Swordwrath():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ОПИСАНИЕ$Лёгкий ближний боец Империи Порядка с низким здоровьем. Вооружён массивным мечом для ближнего боя. Эффективен против тяжёлых юнитов, но уязвим к дальнобойным атакам.$СПОСОБНОСТИ$Прыжок: Совершает рывок вперёд и оглушает первого врага, в которого врезается.$Перезарядка: 30 сек.$ЛОР$Мечегневы следуют учению «Путь Меча». Основаны Генералом Гневнаром, а его преемником стал принц Ксифос.', image='swordwrath.png', log=is_login)

@app.route('/archidon')
def Archidon():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ОПИСАНИЕ$Лёгкий дальнобойный юнит Империи Порядка с низким здоровьем. Вооружён большим луком, чтобы поражать врагов на расстоянии. Эффективен в большом количестве и против лёгких юнитов.$ЛОР$Архидоны следуют учению «Путь Лука». Основаны Великим мастером лука Архисом, а его преемницей стала принцесса Китчу.', image='archidon.png', log=is_login)

@app.route('/eclipsor')
def Eclipsor():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ОПИСАНИЕ$Лёгкий летающий дальнобойный юнит Хаотической Империи с низким здоровьем. Использует мощный лук для атак с воздуха. Особенно эффективен против лёгких юнитов.$КЛЮЧЕВЫЕ ОСОБЕННОСТИ:$Воздушная мобильность$Специализация против лёгких целей$Уязвимость к зенитным атакам', image='eclipsor.png', log=is_login)

@app.route('/shadowrath')
def Shadowrath():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ОПИСАНИЕ$Лёгкий ближний боец Империи Порядка со средним запасом здоровья. Использует скорость и ловкость для уничтожения врагов. Эффективен против лёгких юнитов.$СПОСОБНОСТИ$Парирование: Блокирует входящие эффекты урона, такие как оглушение.$Перезарядка: 4 сек.$ПАССИВНЫЕ СПОСОБНОСТИ$Зацикленность: Последовательные атаки по одной цели увеличивают урон на 5 единиц за стак (максимум 3 стака).$ИСТОРИЯ$Основаны принцессой Шейд, также известной как «Тень». Теневые клинки — элитные убийцы, которых традиционно отбирают из лучших воинов ордена Мечегневов.$Изначально формирование существовало в тени, борясь против Благородного Синдиката, чья власть душила города Инаморты.$После серии успешных операций в столице Порядка принцесса раскрыла своё руководство отрядом и официально передала Теневые клинки своему отцу, королю Зареку, усилив его армию накануне Второй Великой войны.', image='shadowrath.png', log=is_login)

@app.route('/spearton')
def Spearton():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ОПИСАНИЕ$Тяжёлый ближний боец Империи Порядка с большим запасом здоровья. Вооружён мощным копьём и прочным щитом. Особенно эффективен против лёгких юнитов.$СПОСОБНОСТИ$Блок:$ Переходит в защитную стойку, снижая получаемый урон, но замедляя скорость передвижения и атак.$ИСТОРИЯ$Копейщики исповедуют философию «Путь Копья». Орден основан генералом Копраксом, после него руководство перешло к принцу Адикаю, а затем — к принцу Атрейосу.', image='spearton.png', log=is_login)

@app.route('/juggerknight')
def Juggerknight():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ОПИСАНИЕ$Тяжёлый ближний боец Империи Хаоса с высоким запасом здоровья. Вооружён топором и щитом.$СПОСОБНОСТИ$Рывок:$ Боец устремляется вперёд, оглушая противников и нанося 10 единиц урона. Столкновение с тяжёлым юнитом преждевременно прерывает атаку.$Перезарядка: 35 сек.', image='juggerknight.png', log=is_login)

@app.route('/riprider')
def Riprider():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ОПИСАНИЕ$Кавалерийский боец. Наносит 33% сплэш-урона целям в зоне поражения.', image='riprider.png', log=is_login)

@app.route('/toxic_dead')
def Toxic_dead():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ОПИСАНИЕ$Тяжёлый дальнобойный юнит Хаоса с высоким здоровьем (нежить/токсичный тип).$Компенсирует низкую подвижность ядовитыми атаками. Особенно эффективен против тяжёлых юнитов.$Ключевые особенности:$Токсичный урон (игнорирует часть брони)$Замедляющие яды (контроль толпы)$Уязвимость к огненным/священным атакам', image='toxic_dead.png', log=is_login)

@app.route('/enslaved_giant')
def Enslaved_giant():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ОПИСАНИЕ$Гигантский юнит Империи Порядка с чрезвычайно высоким запасом здоровья. Использует свою огромную силу и размеры для метания валунов во врагов.$СПОСОБНОСТИ$Установка катапульты: Укрепившись на позиции, Порабощённый Гигант получает:$+25% к дальности атаки$+33% к урону$+10% к сплэш-урону$(Требуется: Кузница 1 уровня)$Тактические особенности:$Медлительность компенсируется разрушительной силой$Эффективен против укреплений и скоплений войск$Требует поддержки из-за уязвимости при "установке"', image='enslaved_giant.png', log=is_login)

@app.route('/giant')
def Giant():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ОПИСАНИЕ$Гигантский юнит Хаотической Империи с чрезвычайно высоким запасом здоровья.$Использует свою огромную силу и размеры для сокрушительных атак по площади. Чрезвычайно эффективен против тяжёлых юнитов.$Ключевые характеристики:$Сокрушающие удары (урон по области)$Абсолютная мощь против бронетехники и укреплений$Ограниченная мобильность (медленное передвижение)$Тактическое применение:$Идеален для прорыва вражеских формирований$Требует поддержки против скоростных юнитов$Может использоваться как "живая таранная машина"', image='giant.png', log=is_login)

@app.route('/meric')
def Meric():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ОПИСАНИЕ$Лёгкий магический юнит поддержки Империи Порядка со средним запасом здоровья. Использует заклинания для лечения союзников и создания барьера против снарядов.$СПОСОБНОСТИ$Лечение: Восстанавливает здоровье выбранному союзному юниту.$Перезарядка: 1 сек.$Щит: Создаёт защитный барьер вокруг Мэрика, блокирующий все снаряды.$Требование: Храм 1 уровня$Перезарядка: 22 сек.$Тактическая роль:$Приоритетный целитель (быстрое восстановление)$Анти-артиллерийская защита (узкоспециализированный щит)$Хрупкость (требует прикрытия)$Оптимальное использование:$В паре с тяжёлыми юнитами$Против массовых лучников/метательных войск$В обороне ключевых точек', image='meric.png', log=is_login)

@app.route('/magikill')
def Magikill():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ОПИСАНИЕ$Лёгкий магический юнит Империи Порядка с низким здоровьем. Владеет мощными заклинаниями площадного действия и способностью призывать миньонов.$СПОСОБНОСТИ$Призыв миньона: Создаёт магического ближнего бойца.$Перезарядка: 8 сек.$Фульминат: Мощный взрыв, наносящий урон по области и оглушающий поражённых юнитов.$Перезарядка: 5 сек.$Улучшение:$+1 к максимальному количеству миньонов (требуется Храм 2 уровня)$Тактическое применение:$Контроль толпы (оглушение + отвлекающие миньоны)$Хрупкий, но высокий урон в аое$Масштабируется с улучшениями', image='magikill.png', log=is_login)

@app.route('/illuminate')
def Illuminate():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ОПИСАНИЕ$На 10 секунд раскрывает всю карту боя, включая ресурсы противника и численность его армии.$Также даёт ускорение магическим юнитам на 15 секунд.$Тактическое применение:$Разведка: Видимость всей карты и экономики врага$Синергия: Ускорение магов для контратак/отступления$Окно уязвимости: Кратковременный эффект требует точного времени активации$Рекомендации:$Использовать перед ключевыми атаками$Комбинировать с магическими юнитами для максимального эффекта$Против скрытых стратегий/стелс-юнитов', image='illuminate.png', log=is_login)

@app.route('/miner_hustle')
def Miner_hustle():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ОПИСАНИЕ$Увеличивает скорость шахтёров на 50% на 10 секунд.$Практическое применение:$Ускоренная добыча ресурсов в критический момент$Быстрая эвакуация с передовых шахт при атаке$Синергия с другими экономическими баффами', image='miner_hustle.png', log=is_login)

@app.route('/rage')
def Rage():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ЯРОСТЬ$ОПИСАНИЕ$Увеличивает скорость атаки и передвижения лёгких юнитов на 25% на 5 секунд.$Тактическое применение:$Кратковременный, но мощный буст для агрессивных тактик$Идеально для:$▸ Заливки противника дешёвыми юнитами$▸ Финишных атак на убегающего врага$▸ Спасения своих отрядов от окружения$Особенности:$⚠️ Короткая длительность — требует точного времени активации$⚡ Синергия с массовыми легкими юнитами (типа Swordwrath)', image='rage.png', log=is_login)

@app.route('/surge')
def Surge():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ВОЛНА$ОПИСАНИЕ$Увеличивает длительность эффектов стихий на 50% и частоту нанесения урона на 50% на 10 секунд.$Тактическое применение:$Усиливает огненные/ядовитые/электрические эффекты$Комбинируется с DoT-способностями (урон в секунду)$Оптимально для:$▸ Босс-файтов (пролонгация горения/шока)$▸ Контроля толпы (замедления/станы)$▸ Синергии с магическими билдами$⚠️ Не влияет на чистый физический урон$⚠️ Требует активных статусов на цели', image='surge.png', log=is_login)

@app.route('/tesla_coil')
def Tesla_coil():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='КАМЕРА ТЕСЛА$ОПИСАНИЕ$Преобразует захваченную Центральную башню в мощную электрическую башню, которая разряжает молнии.$Перезарядка: 60 сек.$Механика:$Требует контроля центральной точки карты$Наносит периодический урон по области (электрические разряды)$Эффективна против:$▸ Групповых атак (замедление + цепные разряды)$▸ Техники/брони (дополнительный урон к механизмам)$Особенности:$⚠️ Ограничение: Не действует под землей', image='tesla_coil.png', log=is_login)

@app.route('/acid_rain')
def Acid_rain():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ТОКСИЧНЫЙ ДОЖДЬ$ОПИСАНИЕ$Призывает кислотный дождь, который отравляет обычные юниты (не-токсичные). Нежить получает бонус к скорости в зоне дождя.$Особенности:$Не покрывает базы (ваша и вражеская)$Перезарядка: 60 сек$▸ Механика:$• Ядовитый урон: Постепенный урон по времени$• Бонус нежити: + к скорости движения (только в зоне дождя)$• Иммунитеты: Токсичные юниты не получают урона$▸ Тактическое применение:$✓ Контроль зон (ресурсные точки)$✓ Синергия с нежитью (атака + ускорение)$✓ Блокировка вражеского пуша (но не баз!)', image='acid_rain.png', log=is_login)

@app.route('/heavy_healing_wisp')
def Heavy_healing_wisp():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ТЯЖЁЛЫЙ ЦЕЛИТЕЛЬНЫЙ ВИСП$ОПИСАНИЕ$Создает целебный огонёк, который лечит один тяжёлый юнит со скоростью 25 HP/сек в течение 10 секунд.$Перезарядка: 60 сек.$▸ Особенности:$• Таргетинг: Автоматически выбирает раненого тяжёлого юнита в радиусе$• Непрерывное лечение: 250 HP за полный цикл (10 сек × 25 HP)$▸ Тактическое применение:$✓ Спасение дорогих тяжёлых единиц (гиганты/танки)$✓ Комбо с устойчивыми юнитами (щитоносцы/боссы)$✓ Не эффективен против:$Массового урона (лечит только 1 цель)$Мгновенного убийства (нужно время)', log=is_login)

@app.route('/lightning_storm')
def Lightning_storm():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ГРОЗОВОЙ ШТОРМ$ОПИСАНИЕ$Создает грозовой фронт, который формирует медленно движущееся грозовое облако, поражающее врагов молниями.$Перезарядка: 60 сек.$▸ Особенности:$• Наносит периодический урон по области$• Приоритетные цели: сгруппированные юниты$▸ Тактика:$✓ Идеален для защиты ключевых точек$✓ Бесполезен против подземных юнитов', log=is_login)

@app.route('/projectile_barrier')
def Projectile_barrier():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='БАРЬЕР ОТ СНАРЯДОВ$ОПИСАНИЕ$Создает защитный щит на передовой линии вашей армии, который блокирует все снаряды в течение 12 секунд.$Перезарядка: 60 сек.$▸ Ключевые свойства:$• Полная защита от:$Стрел$Магических снарядов$Метательных снарядов$• Не эффективен против:$Ближних атак$Заклинаний, действующих через барьер$▸ Тактическое применение:$✓ Прикрытие штурмовых отрядов$✓ Контроль против лучников/некоторых магов$✓ Синергия с:$• Щитоносцами (двойная защита)$• Магами (безопасное применение заклинаний)', log=is_login)

@app.route('/snow_squall')
def Snow_squall():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='СНЕЖНЫЙ ШКВАЛ$ОПИСАНИЕ$Создает снежный шторм, который замедляет поражённых юнитов. Действует в течение 15 секунд.$Перезарядка: 60 сек.$▸ Тактическое применение:$✓ Сдерживание атакующих сил противника$✓ Синергия с:$Мобильными юнитами (обход замедленных врагов)$✓ Неэффективен против:$Юнитов с иммунитетом к холоду$Подземных/летающих целей', log=is_login)

@app.route('/healing_ward')
def Healing_ward():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ЛЕЧЕБНЫЙ ТОТЕМ$ОПИСАНИЕ$Исцеляет союзные юниты в радиусе действия. Действует 15 секунд.Перезарядка: 45 сек.$▸ Тактическое применение:$✓ Поддержка при удержании позиций$✓ Комбинации с:$Танками (продление их живучести)$Групповыми построениями', log=is_login)

@app.route('/scorch')
def Scorch():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ОЖОГ$ОПИСАНИЕ$Каждые 5 секунд увеличивает длительность эффекта на 1 секунду. Призывает град комет, падающих в течение 2 секунд.$Поражённые цели получают средний урон, оглушение и горение. Максимальная длительность — 50 секунд. 10 стаков создают 10-кратный поток комет.Перезарядка: 5 сек.$▸ Механика:$• Нарастающий эффект:$1 стак = +1 сек (макс. 50 сек)$• Воздействие:$Урон: Средний + доп. урон от горения$▸ Оптимальное использование:$✓ Удержание точек (чистка зоны)$✓ Прорыв обороны (массовый контроль)$✓ Эффективен против:$Скоплений пехоты$Статичных построек$▸ Ограничения:$⚠️ Требует времени для раскрытия потенциала$⚠️ Эффективность снижается против Мобильных юнитов', log=is_login)

@app.route('/boyers_trap')
def Boyers_trap():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ЛОВУШКА ОХОТНИКА$ОПИСАНИЕ$После смерти Архидонов остаётся ловушка. Активируется при приближении врагов, сковывая их верёвкой на короткое время.$Архидоны получают +10% к здоровью. (Требуется: Оружейная 1 ур.)$▸ Механика:$• Активация: Срабатывает при приближении врага$• Эффект - Обездвиживание$• Бонус: +10% HP для всех Архидонов (пассив)$▸ Тактическое применение:$✓ Замедление вражеского преследования$✓ Защита тыловых лучников$✓ Синергия с:$Засадными тактиками$Ловушками других типов$▸ Ограничения:$⚠️ Одноразовая (исчезает после срабатывания)$⚠️ Бесполезна против летающих юнитов', log=is_login)

@app.route('/brilliance')
def Brilliance():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ВЕЛИКОЛЕПИЕ$ОПИСАНИЕ$Снижает стоимость исследований улучшений на 25%.$Уменьшает стоимость создания магических юнитов на 25%.$▸ Эффекты:$• Экономия ресурсов$• Накопительный эффект:$Можно комбинировать с другими экономическими бонусами$▸ Стратегическое значение:$✓ Ускорение технологического прогресса$✓ Массовый найм магов$✓ Критичен для:$Магических билдов$Позднеигровых стратегий', log=is_login)

@app.route('/castle_archer')
def Castle_archer():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ЗАМКОВЫЙ ЛУЧНИК$ОПИСАНИЕ$Лимит на поле боя: 2$Позволяет тренировать Замковых Лучников — лёгких дальнобойных юнитов Империи Порядка. Вооружены усиленными луками для поражения целей из-за укреплений.$▸ Особенности:$• Постоянное присутствие:$Остаются на поле боя между волнами атак$Автоматически занимают оборонительные позиции$• Требования постройки:$1 лучник (Бастион 1 ур.)$2 лучника (Бастион 2 ур.)$▸ Тактическое применение:$✓ Защита ключевых точек', log=is_login)

@app.route('/enchanted_pike')
def Enchanted_pike():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ВОЛШЕБНЫЕ ПИКИ$ОПИСАНИЕ$Удваивает длину копий копейщиков$+10 к урону наконечника$Открывает доступ к дальнобойным чарам$Требования:$Оснащение всех копейщиков длинными пиками (Кузница 1 ур.)$Применение дальнобойных чар для копейщиков (Храм 2 ур.)$▸ Эффекты улучшения:$• Новые возможности атаки:$Увеличенная дистанция боя (в 2 раза)$Специальный бонусный урон (+10) при точном попадании$• Магические модификации:$Возможность наложения чар$Чары действуют на расстоянии$▸ Тактическое применение:$✓ Идеально для удержания оборонительных позиций$✓ Эффективно против кавалерии и тяжелых юнитов$✓ Особенно полезно в сочетании с магами-зачарователями$▸ Особенности:$Копейщики становятся гибридом ближнего/дальнего боя$Увеличивает стратегическую ценность копейщиков', log=is_login)

@app.route('/mana_burst')
def Mana_burst():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='МАГИЧЕСКИЙ ВЗРЫВ$ОПИСАНИЕ$Сокращает время восстановления способностей юнитов Порядка на 15%$При смерти Магикала создает взрыв, наносящий 100 урона врагам в области$При смерти Мерика создает область исцеления, восстанавливающую 100 здоровья$▸ Тактическое применение:$✓ Ускорение перезарядки способностей в критический момент$✓ Дополнительный эффект даже после смерти ключевых юнитов$✓ Особенно полезно:$В массовых сражениях$При контроле территории$▸ Особенности:$Можно комбинировать с другими магическими улучшениями$Эффекты срабатывают автоматически', log=is_login)

@app.route('/miner_upgrade')
def Miner_upgrade():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='УЛУЧШЕНИЕ ШАХТЁРОВ$ОПИСАНИЕ$Открывает возможность исследования улучшений для экономических юнитов.$Уровень 1 (Бастион 1 ур.):$+15% к скорости добычи$+10 к здоровью$Уровень 2 (Бастион 2 ур.):$+30% к скорости добычи$+20 к здоровью$▸ Эффекты улучшения:$• Экономический буст:$Значительно ускоряет сбор ресурсов$Позволяет быстрее развивать экономику$• Выживаемость:$Повышает устойчивость шахтёров к нападениям$▸ Стратегическое значение:$✓ Критически важно для экономических стратегий$✓ Позволяет быстрее наращивать армию$✓ Особенно полезно в длительных играх', log=is_login)

@app.route('/mining_engineer')
def Mining_engineer():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ИНЖЕНЕР-ШАХТЁР$ОПИСАНИЕ$Открывает способность "Возведение стен" для всех экономических юнитов.$▸ Способность "Возведение стен":$Шахтёры и/или Порабощённые шахтёры могут строить улучшаемые стены, которые:$Наносят урон соприкасающимся юнитам каждые 5 секунд$Можно улучшать$Уровень 1 (Кузница 1 ур.):$Здоровье стены: 250$Урон: +2$Уровень 2 (Кузница 2 ур.):$Здоровье стены: 350$Урон: +4$▸ Тактическое применение:$✓ Создание временных укреплений$✓ Замедление вражеского продвижения$✓ Защита ресурсных узлов$▸ Особенности:$Стены могут строить только экономические юниты$Можно комбинировать с другими оборонительными сооружениями', log=is_login)

@app.route('/monstrosity')
def Monstrosity():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('main.html', username=f'{username}', text='ЧУДОВИЩНОСТЬ$ОПИСАНИЕ$Открывает улучшения здоровья для Гигантов и создает отдельную очередь их тренировки.$Улучшения:$• Уровень 1 (Оружейная 1 ур.):$+15% к здоровью Гигантов$• Уровень 2 (Оружейная 2 ур.):$+30% к здоровью Гигантов$▸ Ключевые особенности:$✓ Отдельная очередь производства:$Позволяет параллельно тренировать Гигантов и обычные войска$Ускоряет создание гигантской армии$✓ Значительное усиление выживаемости:$Гиганты становятся настоящими "танками" на поле боя$Эффективность против осадных орудий$▸ Тактическое применение:$Идеально для "танковых" стратегий$Критически важно в поздней игре$Особенно эффективно:$▸ При штурме укреплений$▸ В сочетании с лекарями', log=is_login)

@app.route('/library')
def Library():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    return render_template('view_library.html', pages=pages, username=username, log=is_login)

@app.route('/register', methods=['GET', 'POST'])
def register():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    form = RegisterForm()
    if form.validate_on_submit() and not is_login:
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', username=username, title='Регистрация', form=form, log=is_login)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global user, is_login, username
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'

    form = LoginForm()
    if form.validate_on_submit() and not is_login:
        for us in db_sess.query(User).filter(User.name == form.name.data):
            if check_password_hash(us.hashed_password, form.password.data):
                user = us
                is_login = True
                session['is_login'] = is_login
                username = us.name
                session['username'] = us.name
                return redirect('/')
                return render_template('login.html', title='Вход',
                                   form=form, message="Вы вошли в акк")
            else:
                return render_template('login.html', title='Вход',
                                       form=form, message="А парольчик не тот")
        db_sess.commit()
        return redirect('/')
    return render_template('login.html', title='Вход', form=form, log=is_login)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    global username, user
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'

    form = LoginForm()
    if request.form.keys() and is_login:
        is_login = False
        session['is_login'] = False
        user = None
        username = 'Гость'
        session['username'] = 'Гость'
        session.clear()
        return redirect('/')
    return render_template('logout.html', title='Выход', form=form, log=is_login)

@app.route('/decks')
def View_decks():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    res = []
    for deck in db_sess_deck.query(Deck).all():
        res.append([deck.ch1, deck.ch2, deck.ch3, deck.ch4, deck.ch5, deck.ch6, deck.ch7, deck.ch8])
    return render_template('view_decks.html', decks=res, username=username, log=is_login)
@app.route('/decks/new_deck')
def New_deck():
    try:
        is_login = session['is_login']
        username = session['username']
    except Exception:
        is_login = False
        username = 'Гость'
    filenames = []
    for root, dirs, files in os.walk('static/images/icons'):
        filenames = files
    deck_is_8 = (len(new_deck) == 8)
    return render_template('create_deck.html', username=f'{username}', filenames=filenames, deck=new_deck, full=deck_is_8, log=is_login)

@app.route('/decks/add_card', methods=["POST"])
def Add_card():
    if len(new_deck) < 8:
        for root, dirs, files in os.walk('static/images/icons'):
            for i in files:
                if f'{i}.x' in request.form and i not in new_deck:
                    new_deck.append(i)
    return redirect('/decks/new_deck')

@app.route('/decks/delete_card', methods=["POST"])
def Delete_card():
    for i in new_deck:
        if f'{i}.x' in request.form:
            new_deck.remove(i)
    return redirect('/decks/new_deck')

@app.route('/decks/publish_deck', methods=["GET", "POST"])
def Publish_deck():
    if is_login:
        deck = Deck(author=username, ch1=new_deck[0], ch2=new_deck[1], ch3=new_deck[2], ch4=new_deck[3], ch5=new_deck[4], ch6=new_deck[5], ch7=new_deck[6], ch8=new_deck[7])
        db_sess_deck.add(deck)
        db_sess_deck.commit()
    return redirect('/decks/new_deck')




if __name__ == '__main__':
    main()