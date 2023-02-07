### Запуск приложения

    git clone https://github.com/gmoroz/stay_vacay_backend
    cd stay_vacay_backend
    docker-compose -f docker-compose-backend.yaml up -d

Документация будет доступна по адресу `http://localhost:8089/docs`

### Остановка приложения:
Если надо удалить данные бд, добавьте в конце команды флаг `-v`

    docker-compose -f docker-compose-backend.yaml down 
