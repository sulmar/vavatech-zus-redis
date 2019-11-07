# REDIS

## Komendy

### Connection

| Komenda  | Opis   |
|---|---|
| **AUTH** [password] | Autentykacja do serwera  |
| **PING** [message] | Ping do serwera  |
| **ECHO** message | Wyświetlenie komunikatu |
| **SELECT** index | Zmiana bazy danych |
| **SWAPDB** index index | Zamiana baz danych |
| **QUIT** | Zamknięcie połączenia |
| **INFO** [section] | Wyświetlenie informacji |

### Keys

| Komenda  | Opis   |
|---|---|
| **DEL** key  | Usunięcie klucza  |
| **DUMP** key  | Pobranie serializowanej wartości klucza  |
| **EXISTS** key  | Sprawdzenie czy klucz istnieje |
| **EXPIRE** key seconds  | Ustawienie czasu wygaśnięcia klucza |
| **EXPIREAT** key timestamp  | Ustawienie daty wygaśnięcia klucza |
| **KEYS** pattern | Wyszukiwanie kluczy według wzorca |
| **MOVE** key db | Przesunięcie klucza do innej bazy danych |
| **PERSIST** key | Wyłączenie wygasania klucza |
| **TTL** key | Pobranie pozostałego czasu do wygaśnięcia klucza w sekundach |
| **PTTL** key | Pobranie pozostałego czasu do wygaśnięcia klucza w milisekundach 
| **RANDOMKEY** | Pobranie losowego klucza |
| **RENAME** key newkey | Zmiana nazwy klucza |
| **TYPE** key  | Pobranie typu klucza |



### Strings

| Komenda  | Opis   |
|---|---|
| **SET** key value | Ustawienie wartości klucza  |
| **GET** key  | Pobranie wartości klucza |
| **GETRANGE** key start end  | Pobranie fragmentu wartości klucza |
| **APPEND** key value | Dołączenie wartości do wartości klucza |
| **MSET** key1 value1 [key2 value2] | Ustawienie wielu wartości kluczy  |
| **MGET** key1 [key2] | Pobranie wielu wartości kluczy  |
| **STRLEN** key | Pobranie długości wartości klucza  |
| **INCR** key | Zwiększenie wartości klucza o 1  |
| **INCRBY** key increment | Zwiększenie wartości klucza o podaną wartość |
| **INCRBYFLOAT** key increment | Zwiększenie wartości klucza o podaną wartość ułamkową |
| **DECR** key | Zmniejszenie wartości klucza o 1 |
| **DECRBY** key increment | Zmniejsze wartości klucza o podaną wartość |

### Hashes

| Komenda  | Opis   |
|---|---|
| **HSET** key field value | Ustawienie wartości pola danego klucza  |
| **HMSET** key field value | Ustawienie wielu wartości pola danego klucza  |
| **HGET** key field  | Pobranie wartości pola danego klucza |
| **HMGET** key field [field ...] | Pobranie wartości wybranych pól danego klucza |
| **HGETALL** key  | Pobranie wszystkich pól danego klucza |
| **HKEYS** key  | Pobranie kluczy danego klucza |
| **HVALS** key  | Pobranie wartości danego klucza |
| **HINCRBY** key field increment  | Inkrementacja wartości pola |
| **HDEL** key  | Usunięcie klucza |
| **HEXISTS** key field | Sprawdzenie czy pole istnieje w danym kluczu |
| **HSCAN** key cursor | Pobranie pól i wartości kluczy |
| **HSTRLEN** key field | Pobranie długości wartości pola |



### Sets

| Komenda  | Opis   |
|---|---|
| **SADD** key member [member] | Dodanie elementu do zbioru  |
| **SMEMBERS** key | Pobranie elementów ze zbioru |
| **SCARD** key | Pobranie ilości elementów w zbiorze |
| **SMOVE** source destination member | Przesunięcie elementu pomiędzy zbiorami |
| **SISMEMBER** key member | Sprawdzenie czy wartość jest elementem zbioru |
| **SREM** key member | Usunięcie elementu ze zbioru |
| **SPOP** key [count] | Usunięcie i pobranie pojedyńczego lub większej ilości losowych elementów ze zbioru |
| **SRANDMEMBER** key [count] | Pobranie pojedyńczego lub większej ilości losowych elementów ze zbioru |
| **SUNION** key [key] | Suma zbiorów |
| **SUNIONSTORE** destination key [key] | Suma zbiorów i zapisanie ich pod nowym kluczem |
| **SINTER** key [key] | Część wspólna zbiorów |
| **SINTERSTORE** desitination key [key] | Część wspólna zbiorów i zapisanie ich pod nowym kluczem |
| **SDIFF** key [key] | Różnica zbiorów |
| **SDIFFSTORE** desitination key [key] | Różnica zbiorów i zapisanie ich pod nowym kluczem |


### Sorted Sets

| Komenda  | Opis   |
|---|---|
| **ZADD** key score member | Dodanie elementu do zbioru  |
| **ZREM** key member | Usunięcie elementu do zbioru  |
| **ZINCRBY** key increment member | Zwiększego wartości klucza w zbiorze  |
| **ZSCORE** key member | Pobranie wyniku elementu ze zbioru  |
| **ZSCAN** key cursor | Pobranie elementów ze zbioru |
| **ZCARD** key | Pobranie ilości elementów ze zbioru |
| **ZCOUNT** key min max | Pobranie ilości elementów ze zbioru, których wynik jest pomiędzy wartościami min i max |
| **ZRANK** key member | Pobranie rankingu na podstawie wyniku od najniższej wartości |
| **ZREVRANK** key member | Pobranie rankingu na podstawie wyniku od najwyższej wartości |
| **ZRANGEBYSCORE** key min max [withscores] | Pobranie elementów w zakresie rankingu |


### Lists

| Komenda  | Opis   |
|---|---|
| **LPUSH** key value [value] | Wstawaienie elementu na początek listy  |
| **RPUSH** key value [value] | Wstawaienie elementu na koniec listy |
| **LRANGE** key start stop  | Pobranie fragmentu elementów listy |
| **LREM** key count value  | Usunięcie określonej ilości elementów z listy począwszy od podanej wartości |
| **LPOP** key  | Pobranie i usunięcie elementu z góry |
| **RPOP** key  | Pobranie i usunięcie elementu z dołu |
| **RPOPLPUSH** key  | Przenosi ostatni element pomiędzy listami i zwraca go |
| **LLEN** key  | Pobranie ilości elementów listy |
| **LTRIM** key start stop | Wycina fragment listy |

### Geo

| Komenda  | Opis   |
|---|---|
| **GEOADD** key longitude latitude member | Dodanie pozycji elementu |
| **GEOPOS** key member  | Pobranie pozycji elementu |
| **GEODIST** key member1 member2 [unit] ]| Obliczenie odległości pomiędzy elementami |
| **GEORADIUS** key longitude latitude radius   | Wyszukiwanie elementów w określonym promieniu od podanej lokalizacji |
| **GEORADIUSBYMEMBER** key member radius   | Wyszukiwanie elementów w określonym promieniu od podanego elementu |

### Bitmaps

| Komenda  | Opis   |
|---|---|
| **SETBIT** key offset value | Ustawienie bitu |
| **SETBIT** key offset | Pobranie bitu |
| **BITOP** operation destkey key | Przetworzenie operacji bitowych |
| **BITCOUNT** key [start end] | Obliczenie ilości ustawionych bitów na 1 |
| **BITPOS** key [start] [end] | Pobranie pozycji bitu ustawionego na 1 |

 
 ### Transakcje

| Komenda  | Opis   |
|---|---|
| **MULTI**  | Rozpoczęcie bloku transakcji |
| **EXEC** | Wykonanie wszystkich komend |
| **DISCARD** | Porzucenie wszystkich komend |
| **WATCH** key [key] | Założenie blokady |
| **UNWATCH** | Zwolnienie wszystkich blokad |


### Pub/Sub

| Komenda  | Opis   |
|---|---|
| **SUBSCRIBE** channel [channel ...] | Nasłuchiwanie komunikatów publikowanych do podanego kanału |
| **PUBLISH** channel message | Wysłanie komunikatu na kanał |
| **UNSUBSCRIBE** [channel] | Zatrzymanie nasłuchiwania komunikatów |
| **PSUBSCRIBE** pattern [pattern] | Nasłuchiwanie komunikatów według wzorca |

### Stream

| Komenda  | Opis   |
|---|---|
| **XADD** key ID field string [field string...] | Pisanie do strumienia |
| **XREAD** [count] STREAMS key ID | Czytanie ze strumienia |
| **XLEN** key | Pobranie długości strumienia |




## Instalacja Redis

### Docker

- Pobranie obrazu
~~~
docker pull redis:latest
~~~

- Wyświetlenie pobranych obrazów
~~~
docker images
~~~

- Uruchomienie kontenera
~~~
docker run --name zus-redis -d -p 6379:6379 redis
~~~

- Wyświetlenie uruchomionych kontenerów
~~~
docker ps
~~~

- Uruchomienie trybu interaktywnego
~~~
docker exec -it zus-redis redis-cli
~~~

- Uruchomienie kontenera
~~~ bash
docker start zus-redis 
~~~

- Zatrzymanie kontenera
~~~ bash
docker stop zus-redis
~~~

- Usunięcie kontenera
~~~ bash
docker rm zus-redis
~~~


## Podstawy

- Sprawdzenie czy serwer działa
~~~
PING
~~~

- Wyświetlenie komunikatu
~~~ 
ECHO 'Hello World'
~~~

- Wyczyszczenie konsoli
~~~
CLEAR
~~~

- Wyjście z konsoli
~~~
QUIT
~~~

- Włączenie śledzenia
~~~
MONITOR
~~~

- Wyświetlenie informacji o serwerze
~~~
INFO Server
~~~


## Strings

- do 2^32 bitów (512MB) na każdy klucz
- zastosowania
    - czysty tekst (cache strony)
    - obiekty json
    - surowe bity/flagi (dzienna aktywność użytkowników)
    - zawartość binarnych plików (operacje na nich)


- Ustawienie wartości klucza (liczba)

~~~
SET foo 100
GET foo
~~~

- Ustawienie wartości klucza (tekst)
~~~
SET bar "Hello World"
GET bar
~~~


- Zapisanie json
~~~
SET users:marcin "{\"firstname\":\"Marcin\",\"lastname\":\"Sulecki\",\"email\":\"marcin.sulecki@sulmar.pl\"}"
~~~

- Sprawdzenie czy klucz istnieje
~~~
EXISTS foo
~~~

- Usunięcie klucza
~~~
DEL foo
~~~

- Usunięcie klucza bez blokowania
~~~
UNLINK bar
~~~
Komenda odpina klucz z przestrzeni roboczej. Faktyczne usunięcie nastąpi później asynchronicznie (w osobnym wątku).


- Pobranie kluczy
~~~
KEYS *
~~~

- Pobranie kluczy ze stronicowaniem
~~~
SCAN 0 COUNT 10
SCAN 7 COUNT 5
~~~

- Pobranie kluczy ze stronicowaniem i filtrowaniem
~~~
SCAN 0 COUNT 10
~~~

- Nadpisanie wartości klucza
~~~
SET bar "Hello Redis"
GET bar
~~~

- Zabezpieczenie przed nadpisaniem
~~~
SET bar "Hello NoSQL" NX
GET bar
~~~

- Ustawienie wartości klucza tylko jeśli istnieje
~~~
SET message "Hello John" XX
EXISTS 
~~~

- Sprawdzenie typu 
~~~
TYPE foo
TYPE bar
~~~

- Inkrementacja wartości
~~~
INCR foo
GET foo
~~~

- Dekrementacja wartości
~~~
DECR foo
GET foo
~~~

- Inkrementacja wartości o podaną wartość
~~~
INCRBY foo 10
GET foo
~~~

- Dekrementacja wartości o podaną wartość
~~~
DECRBY foo 10
GET foo
~~~


- Inkrementacja wartości rzeczywistej
~~~
SET room1:temp 21.45
INCRBYFLOAT room1:temp 0.5
INCRBYFLOAT room1:temp -0.25
~~~

- Wyczyszczenie wszystkich kluczy
~~~
FLUSHALL
~~~

- Ustawianie kluczy z przestrzenią nazw

~~~
SET server:name server1
GET server:name
SET server:port 5000
GET server:port
~~~

- Ustawienie wygaśnięcia klucza 
~~~
SET greeting "Hello World"
EXPIRE greeting 50
TTL greeting
~~~

- Ustawienie klucza, który wygaśnie
~~~
SETEX greeting 30 "Hello World"
TTL greeting
~~~

- Ustawienie klucza, który wygaśnie
~~~
SET greeting "Hello World" EX 30
TTL greeting
~~~

- Ustawienie klucza, który wygaśnie o podanej godzinie.
Czas podawany jest w formacie Unix timestamp (ilość sekund od 1970-01-01)
~~~
SET ticket "redis"
EXPIREAT ticket 1573041600
TTL ticket
~~~

Konwerter
https://www.epochconverter.com/


- Usunięcie wygaśnięcia klucza
~~~
PERSIST greeting
TTL greeting
~~~

- Ustawienie wielu wartości
~~~ 
MSET key1 "Hello" key2 "World"
GET key1
GET key2
~~~

- Pobranie wielu wartości
~~~
MGET key1 key2
~~~

- Dopisanie wartości
~~~
APPEND key1 " World"
~~~

- Pobranie zakresu wartości
~~~
SET message "Hello World"
GETRANGE message 0 4
GETRANGE message 6 10
~~~

- Zmiana nazwy klucza
~~~
RENAME key1 greeting
~~~

### Zadania

- Zadanie #1
  
_Utwórz listę uczestników naszego szkolenia w formacie  redis:member1, redis:member2, itd., która zostanie usunięta wraz z zakończeniem szkolenia_


## Lists

- Do 2^32 elementów w każdym kluczu
- zastosowania
    - kolejka
    - stos
    - topN
    - ostatnie wiadomości

- Wstawienie elementów na początek listy
~~~
LPUSH people "John"
LPUSH people "Tom"
LPUSH people "Jenny"
~~~

- Pobranie wszystkich elementów
~~~
 LRANGE people 0 -1
~~~


- Pobranie zakresu elementów
~~~
 LRANGE people 1 2
~~~

- Pobranie elementu z listy o podanym indeksie
~~~
LINDEX people 2
~~~

- Ustawienie wartości pod podanym indeksem
~~~
LSET people 1 Jerry
~~~

- Wstawienie elementów na koniec listy
~~~
RPUSH people Harry
~~~

- Pobranie ilości elementów listy
~~~
LLEN people
~~~

- Pobranie i usunięcie elementu z góry
~~~
LPOP people
~~~

- Pobranie i usunięcie elementu z dołu
~~~
RPOP people 
~~~

- Wstawienie elementu do listy
~~~
LINSERT people BEFORE "John" "Kate"
~~~

Usunięcie określonej ilości elementów z listy począwszy od podanej wartości
~~~
LREM people 2 John 
~~~

Wycina fragment listy
~~~
LTRIM
~~~

- Usunięcie ostatniego elementu z listy, dołączenie go do innej listy i zwrócenie

~~~
LPUSH ordered "order-1"
LPUSH ordered "order-2"
LPUSH ordered "order-3"
RPOPLPUSH ordered delivered
~~~


### Zadania


- Zadanie #2

_ZUS otworzył nowy oddział, w którym posiada 3 stanowiska do obsługi petentów. 
Petenci są obsługiwani zgodnie z kolejnością pobranych z systemu biletów.
Przy stanowiskach znajdują się ekrany, które wyświetlają obsługiwany numer._

Stwórz rozwiązanie, które zrealizuje obsługę.

- Zadanie #3
  
_Dział analiz chce na bieżąco śledzić ilość załatwionych spraw w każdym okienku danego dnia._


## Sets

Zbiory w Redisie to nieuporządkowana kolekcja **unikalnych** elementów (strings).
Możliwe jest dodawanie, usuwanie i sprawdzanie istnienia elementów.

- Do 2^32 elementów w każdym kluczu
- zastosowania
    - przechowywanie relacji (znajomi, followers)


- Dodanie elementów do zbioru
~~~ 
SADD page:home:uniquevisitors:20191106 100.43.12.50
SADD page:home:uniquevisitors:20191106 100.43.14.20
SADD page:home:uniquevisitors:20191106 100.223.14.6
~~~

- Pobranie elementów ze zbioru
~~~
SMEMBERS page:home:uniquevisitors:20191106 
~~~

- Pobranie ilości elementów
~~~
SCARD page:home:uniquevisitors:20191106 
~~~

- Przesunięcie elementu pomiędzy zbiorami
~~~
SADD online user1 user2 user3
SADD offline user4 user5
SMOVE online offline user1
~~~

- Sprawdzenie czy wartość jest elementem zbioru
~~~
SISMEMBER online user2
~~~

- Usunięcie elementu ze zbioru
~~~
SREM online user1
~~~

- Pobranie losowego elementu ze zbioru 
~~~
SADD users user1 user2 user3 user4 user5 
SRANDMEMBER users
~~~

- Pobranie i usunięcie losowego elementu ze zbioru 
~~~
SPOP users
~~~



- Zadanie #3
  
_Utwórz listę uczestników naszego szkolenia w formie listy 


### Operacje na zbiorach

- Suma zbiorów
~~~
SUNION online offline
~~~

- Suma zbiorów i zapisanie ich pod nowym kluczem
~~~
SUNIONSTORE all online offline
~~~

- Część wspólna zbiorów
~~~
SADD warszawa company1 company2 company3 company4
SADD bydgoszcz company2 company3 company5 
SINTER warszawa bydgoszcz
~~~

- Część wspólna zbiorów i zapisanie ich pod nowym kluczem
~~~
SINTERSTORE common online offline
~~~

-- Różnica zbiorów
~~~
SDIFF warszawa bydgoszcz
~~~

-- Różnica zbiorów i zapisanie ich pod nowym kluczem
~~~
SDIFFSTORE diff online offline
~~~


## Sorted Sets

- Sprawdzenie czy element istnieje na liście

- zastosowania
  - tablica wyników gry


Dodanie elementów
~~~
ZADD skills:marcin 100 csharp
ZADD skills:marcin 94 wpf
ZADD skills:marcin 2 python
~~~


- Pobranie rankingu podanego klucza 
~~~
ZSCORE skills:marcin csharp
~~~

- Pobranie elementów wg rankingu
~~~
ZRANGEBYSCORE skills:marcin 50 100
~~~

- Zwiększenie rankingu 
~~~ 
ZINCRBY skills:marcin 1 wpf  
~~~

- Usunięcie elementu
~~~
ZREM skills:marcin python
~~~

- Pobranie ilości elementów
~~~
ZCARD skills:marcin 
~~~


## Hash
Bardzo podobne do tabeli w bazach danych SQL

Jeśli chcesz zmodyfikować cały obiekt zwykły string wystarczy:
~~~
SET user:marcin { 'name':'Marcin Sulecki', 'email': 'marcin.sulecki@gmail.com'}
~~~

Natomiast w przypadku, gdy chcesz mieć dostęp do pojedynczych pól lepszym rozwiązaniem będą tablice asosjacyjne

- Dodanie wartości
~~~
HSET user:marcin name "Marcin Sulecki"
HSET user:marcin email marcin.sulecki@gmail.com
HSET user:marcin score 10
~~~

- Dodanie wielu wartości
~~~
HMSET user:john name "John Smith" email john@gmail.com score 5
~~~

- Pobranie wybranego pola
~~~
HGET user:marcin email
~~~

- Pobranie wybranych pól
~~~
HMGET user:marcin name score
~~~

- Pobranie wszystkich pól
~~~
HGETALL user:marcin
~~~

- Pobranie kluczy
~~~
HKEYS user:marcin
~~~

- Pobranie wartości
~~~
HVALS user:marcin
~~~

- Inkrementacja pola
~~~
HINCRBY user:marcin score 5
~~~

- Usunięcie klucza
~~~
HDEL user:john
~~~

- Zadanie
Stwórz spis 3 książek z polami: tytuł, autor, isbn, rok wydania, ilość wypożyczeń 


## Bitmaps

Ustawienie bitu na 1 na określonej pozycji

~~~
SETBIT article1:today 5 1
SETBIT article2:today 5 1
SETBIT article2:today 3 1
SETBIT article2:today 2 1
SETBIT article1:today 2 1
~~~

Pobranie bitu
~~~
GETBIT article1:today 5
~~~

Operacja AND
~~~
BITOP AND readbotharticles article1:today article2:today
GETBIT readbotharticles 2
GETBIT readbotharticles 3
GETBIT readbotharticles 5
~~~

Operacja OR
~~~
BITOP OR readanyarticle article1:today article2:today
GETBIT readanyarticle 2
GETBIT readanyarticle 3
GETBIT readanyarticle 5
~~~

Obliczenie ilości ustawionych bitów na 1
~~~
BITCOUNT readbotharticles
~~~


## Typy przestrzenne

- Dodanie pozycji
~~~
GEOADD vehicles 52.361389 19.115556 Vehicle1
GEOADD vehicles 52.361389 19.115556 Vehicle2
GEOADD vehicles 52.361389 19.115556 Vehicle3
GEOADD vehicles 52.361389 19.115556 Vehicle4
~~~

- Pobranie pozycji określonego klucza
~~~
GEOPOS vehicles Vehicle2
~~~

- Obliczenie dystansu pomiędzy dwoma pozycjami
~~~ 
GEODIST vehicles Vehicle1 Vehicle4 km
~~~

- Wyszukanie pozycji w określonym promieniu
~~~
GEORADIUS vehicles 0 0 200 km
~~~

- Usunięcie elementu
~~~
ZREM vehicles Vehicle2
~~~

### Zadania 


## Pub/Sub

- Utworzenie subskrypcji
~~~
subscribe sensors:temp1
~~~

- Wysłanie wiadomości
~~~
publish sensors:temp1 54.21
~~~

- Usunięcie subskrypcji
~~~
UNSUBSCRIBE
~~~

Utworzenie subskrypcji ze wzorcem 
~~~
psubscribe sensors.temp*
~~~

- Obsługiwane wzorce
~~~
? - pojedynczy znak
* - dowolny ilość znaków
[ae] - zbiór znaków
~~~

## Strumienie

- Pisanie do strumienia
~~~
xadd events * user john action login
xadd events * user john action visit page index.htm
xadd events * user john action purchase item computer
xadd events * user john action purchase item monitor
xadd events * user john action paid amount 1000
~~~

- Czytanie ze strumienia
~~~
xread count 2 streams events 0
xread count 2 streams events 1572983745546-0
~~~

## Backup

- Zapisanie danych na dysku (snapshoth)
~~~
SAVE
~~~

Powstanie plik _var/libs/redis/dump.rdb_

~~~
SAVE 60 1000
~~~


## Transakcje

- Zatwierdzenie transakcji

~~~
MSET john:debet 100 jeny:debet 100
MULTI
DECRBY john:debet 40
INCRBY jeny:debet 40
EXEC 
~~~



- Wycofanie transakcji

~~~
MSET john:debet 100 jeny:debet 100
MULTI
DECRBY john:debet 40
INCRBY jeny:debet 40
DISCARD 
~~~


## Skrypt

- Wykonane wyrażenia
~~~
EVAL "return redis.call('set','foo', 'Hello')"
EVAL "return redis.call('get','foo')" 0 
~~~

- Skrypt LUA

~~~ lua
local msg = "Hello, world!"
return msg
~~~

- Wykonanie skryptu
~~~
redis-cli --eval hello.lua
~~~



## Autoryzacja

- Ustawienie hasła
~~~
CONFIG SET requirepass P@ssw0rd
~~~

- Autoryzacja
~~~
AUTH P@ssw0rd
~~~


- Usunięcie hasła
~~~
CONFIG SET requirepass ""
~~~


## Masowe wstawianie danych

- Pobranie danych
~~~ bash
curl http://antirez.com/misc/female-names.txt --output female-names.txt
~~~

- Dostosowanie pliku
~~~ bash
sed 's/^/SADD members /' female-names.txt  > names.txt
~~~

- Skopiowanie pliku do obrazu Dockera
~~~ bash
docker cp names.txt zus-redis:/data/names.txt
~~~

- Import dnaych z pliku do Redisa
~~~ bash
cat names.txt | redis-cli --pipe
~~~



## Cluster

1. Utwórz podkatalogi na poszczególnych kontenerów

2. Utwórz w podkatalogu plik _redis.conf_
~~~
port 7000
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
appendonly yes
~~~

3. Utwórz plik _Dockerfile_
~~~
FROM redis:latest

EXPOSE 7000
ADD redis.conf /etc/redis/redis.conf
#RUN chown redis:redis /etc/redis/redis.conf
#ADD redis-entrypoint.sh /usr/local/bin/
#RUN chmod +x /usr/local/bin/redis-entrypoint.sh
#ENTRYPOINT ["redis-entrypoint.sh"]
~~~

i tak dalej w poszczególnych podkatalogach. Pamiętaj o zmianie portów 7000 itd.

4. Uruchom polecenie
~~~ bash
docker-compose up --build -d
~~~

5. Utwórz cluster
~~~ bash
docker exec -it redis-1 redis-cli -p 7000 --cluster create 10.0.0.2:7000 10.0.0.3:7001 \
10.0.0.4:7002 10.0.0.5:7003 10.0.0.6:7004 10.0.0.7:7005 \
--cluster-replicas 1
~~~

6. Podłącz się do jednego z masterów
~~~ bash
docker exec -it redis-1 redis-cli -c -p 7000
~~~

7. Utwórz klucze
~~~
SET key1 Hello
SET key2 World
GET key1
GET key2
~~~

8. Posprzątaj po obrazach
~~~ bash
docker-compose down
~~~
