Даний модуль призначений для створення інтерактивної карти, яка відображається як веб-сторінка.
Головним є модуль map_creation.py, який потрібно запустити для роботи.
Користувач вказує, чи хоче він відображати фонову картограму (хороплет) за показником, що відповідає кількості знятих фільмів на певній території.
Також передбачено вибір, чи відображати кругові маркери на найбільших по кількості зйомок міст світу.
Потім користувач вводить слово або назву фільму і на карті будуються маркери з всіма локаціями зйомок цього фільму.

Модуль створює файл в форматі html, в якому присутні такі теги:
В тезі head зберігаються інші елементи, ціль яких допомогти браузеру в роботі з даними:
- тег meta оприділяє метатеги, які призначені для збереження інформації, призначеної для браузерів і пошукових систем.
	В ньому присутні атрибути:
	http-equiv для конвертування метатегу в заголовок HTTP;
	content встановлює значення атрибута, заданого за допомогою http-equiv або name.
	name - ім'я метатега
- тег script призначений для описання скриптів.
	В ньому присутній атрибут:
	src - адреса скрипта з зовнішнього файлу для імпортування в поточний документ
- тег link встановлює зв'язок з зовнішнім документом (наприклад файл зі стилями чи шрифтами).
	В ньому присутні атрибути:
	rel опридіяє відношення між поточним документом і файлом, на який робиться посилання;
	href задає шлях до файлу.
- тег style застосовується для визначення стилів елементів веб-сторінки.
Тег body  призначений для зберігання змісту веб-сторінки, який відображається у вікні браузера:
- div являється блочним елементом і призначений для виділення фрагмента документа для зміни вигляду контенту.
	В ньому присутні атрибути:
	class - оприділяє ім'я класу, яке дозволяє зв'язати тег зі стильовим оформленням;
	id - вказує ім'я стильового ідентифікатора.

Згенерована в даному модулі карта показує фонову картограму, яка дає нам інформацію про те скільки фільмів було відзнято в тій чи іншій країні.
На карті зображена градація зеленого кольору, чим темніша заливка, тим більше фільмів у цьому регіоні. Такий вид карти легко подає інформацію,
та зручний для сприйняття.
Також показано кругові маркери в містах, де найчастіше знімають фільми. Радіус круга залежить від кількості фільмів, що також зручно передає
додаткову інформацію.
На карті зображуються маркери з іконкою камери, які позначають місця зйомок фільму, назву якого відповідає вводу користувача.
А також на маркері показано назву фільму, бо різні фільми можуть мати схожу назву.
"# map_creation"
