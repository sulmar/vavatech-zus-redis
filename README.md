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


## Cluster

https://itsmetommy.com/2018/05/24/docker-compose-redis-cluster/
