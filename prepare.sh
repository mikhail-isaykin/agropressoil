#!/bin/bash

PROJECT_DIR="prodtehmash"
PROJECT_NAME="config"
VENV_DIR="venv"
MEDIA_DIR="media"
STATIC_DIR="staticfiles"
TEMP_DIR="prodtehmash_new"
ZIP_FILE="prodtehmash_new.7z"
ENV_FILE=".env"
GUNICORN_CONF_FILE="gunicorn.conf.py"
REQUIREMENTS_FILE="requirements.txt"
WWW_USER="main"

DATABASE_USER="prodtehmash"
DATABASE_NAME="prodtehmash"
DATABASE_HOST="127.0.0.1"
DATABASE_PORT="5432"

BACKUP_DIR="${PROJECT_DIR}/backups"

COPY_MEDIA_DIR="Yes"
COPY_STATIC_DIR="No"
COPY_ENV_FILE="Yes"
MOVE_ZIP_FILE="No"


user_variables=(
  PROJECT_DIR
  PROJECT_NAME
  VENV_DIR
  TEMP_DIR
  ZIP_FILE
  ENV_FILE
  GUNICORN_CONF_FILE
  REQUIREMENTS_FILE
  WWW_USER
  DATABASE_USER
  DATABASE_NAME
  DATABASE_HOST
  DATABASE_PORT
  BACKUP_DIR
  COPY_MEDIA_DIR
  COPY_STATIC_DIR
  COPY_ENV_FILE
  MOVE_ZIP_FILE
)


RED='\e[31m'
GRN='\e[32m'
YLW='\e[33m'
RST='\e[0m'


TIMESTAMP=$(date +%d%m%y_%H%M%S)


error_exit() {
  echo -e "${RED}Ошибка: ${1}${RST}\n" >&2
  exit 1
}

check_variables() {
  local -n arr="$1"
  for var_name in "${arr[@]}"; do
    local var_value="${!var_name}"
    echo -e "Проверяю переменную ${GRN}${var_name}${RST}..."
    [ ! -z "$var_value" ] || error_exit "Переменная не задана"
  done
}


echo -e "\n${GRN}Начинаю подготовку к обновлению проекта...${RST}"

echo -e "Проверяю настройки скрипта подготовки:"
check_variables user_variables
echo -e "${GRN}Настройки проверены${RST}"

echo -e "Проверяю наличие директории проекта ${GRN}${PROJECT_DIR}${RST}..."
[ -d "$PROJECT_DIR" ] || error_exit "Директория проекта не найдена"
echo -e "${GRN}Проверено${RST}"

echo -e "Проверяю отсутствие файлов во временной директории ${GRN}${TEMP_DIR}${RST}..."
[[ ! -d "$TEMP_DIR" || -z "$(ls -A "$TEMP_DIR")" ]] || error_exit "Временная директория не пуста"
echo -e "${GRN}Проверено${RST}"

echo -e "Проверяю наличие архива проекта ${GRN}${ZIP_FILE}${RST}..."
[ -f "$ZIP_FILE" ] || error_exit "Архив проекта не найден"
echo -e "${GRN}Проверено${RST}"

case "${COPY_MEDIA_DIR,,}" in
  yes|y|true|1)
    echo -e "Проверяю переменную ${GRN}MEDIA_DIR${RST}..."
    [ ! -z "$MEDIA_DIR" ] || error_exit "Переменная не задана"
    echo -e "${GRN}Проверено${RST}"

    echo -e "Проверяю наличие директории медиа файлов ${GRN}${MEDIA_DIR}${RST} в ${GRN}${PROJECT_DIR}${RST}..."
    [ -d "${PROJECT_DIR}/${MEDIA_DIR}" ] || error_exit "Директория не найдена"
    echo -e "${GRN}Проверено${RST}"
    ;;
esac

case "${COPY_STATIC_DIR,,}" in
  yes|y|true|1)
    echo -e "Проверяю переменную ${GRN}STATIC_DIR${RST}..."
    [ ! -z "$STATIC_DIR" ] || error_exit "Переменная не задана"
    echo -e "${GRN}Проверено${RST}"

    echo -e "Проверяю наличие директории статических файлов ${GRN}${STATIC_DIR}${RST} в ${GRN}${PROJECT_DIR}${RST}..."
    [ -d "${PROJECT_DIR}/${STATIC_DIR}" ] || error_exit "Директория не найдена"
    echo -e "${GRN}Проверено${RST}"
    ;;
esac

case "${COPY_ENV_FILE,,}" in
  yes|y|true|1)
    echo -e "Проверяю переменную ${GRN}ENV_FILE${RST}..."
    [ ! -z "$ENV_FILE" ] || error_exit "Переменная не задана"
    echo -e "${GRN}Проверено${RST}"

    echo -e "Проверяю наличие файла переменных окружения ${GRN}${ENV_FILE}${RST} в ${GRN}${PROJECT_DIR}${RST}..."
    [ -f "${PROJECT_DIR}/${ENV_FILE}" ] || error_exit "Файл переменных окружения не найден"
    echo -e "${GRN}Проверено${RST}"
    ;;
esac


echo -e "Создаю папку для резервных копий ${GRN}${BACKUP_DIR}${RST}..."
mkdir -p "$BACKUP_DIR" || error_exit "Не удалось создать папку для резервных копий"
echo -e "${GRN}Создано${RST}"

echo -e "Введите пароль пользователя базы данных ${GRN}${DATABASE_USER}${RST}"
echo -e "Создаю резервную копию данных базы ${GRN}${DATABASE_NAME}${RST}..."
pg_dump -h "$DATABASE_HOST" -p "$DATABASE_PORT" -U "$DATABASE_USER" -a -Fc \
  -f "${BACKUP_DIR}/backup_data_${TIMESTAMP}.dump" "$DATABASE_NAME" \
  || error_exit "Не удалось создать резервную копию данных"
echo -e "${GRN}Резервная копия данных создана: ${BACKUP_DIR}/backup_data_${TIMESTAMP}.dump${RST}"

echo -e "Создаю резервную копию структуры базы ${GRN}${DATABASE_NAME}${RST}..."
pg_dump -h "$DATABASE_HOST" -p "$DATABASE_PORT" -U "$DATABASE_USER" -s \
  -f "${BACKUP_DIR}/backup_schema_${TIMESTAMP}.sql" "$DATABASE_NAME" \
  || error_exit "Не удалось создать резервную копию структуры"
echo -e "${GRN}Резервная копия структуры создана: ${BACKUP_DIR}/backup_schema_${TIMESTAMP}.sql${RST}"


echo -e "Создаю временную директорию ${GRN}${TEMP_DIR}${RST}..."
mkdir -p "$TEMP_DIR" || error_exit "Не удалось создать временную директорию"
echo -e "${GRN}Создано${RST}"

case "${COPY_MEDIA_DIR,,}" in
  yes|y|true|1)
    echo -e "Копирую директорию медиа файлов ${GRN}${PROJECT_DIR}/${MEDIA_DIR}${RST} в ${GRN}${TEMP_DIR}${RST}..."
    cp -r "${PROJECT_DIR}/${MEDIA_DIR}" "$TEMP_DIR" || error_exit "Не удалось скопировать директорию"
    echo -e "${GRN}Скопировано${RST}"
    ;;
  *)
    echo -e "${YLW}Пропускаю копирование директории медиа файлов${RST}"
    ;;
esac

case "${COPY_STATIC_DIR,,}" in
  yes|y|true|1)
    echo -e "Копирую директорию статических файлов ${GRN}${PROJECT_DIR}/${STATIC_DIR}${RST} в ${GRN}${TEMP_DIR}${RST}..."
    cp -r "${PROJECT_DIR}/${STATIC_DIR}" "$TEMP_DIR" || error_exit "Не удалось скопировать директорию"
    echo -e "${GRN}Скопировано${RST}"
    ;;
  *)
    echo -e "${YLW}Пропускаю копирование директории статических файлов${RST}"
    ;;
esac

echo -e "Распаковываю архив проекта ${GRN}${ZIP_FILE}${RST} в ${GRN}${TEMP_DIR}${RST}..."
7z x "$ZIP_FILE" -o"$TEMP_DIR" -y > /dev/null || error_exit "Не удалось распаковать архив"
echo -e "${GRN}Распаковано${RST}"

case "${MOVE_ZIP_FILE,,}" in
  yes|y|true|1)
    echo -e "Перемещаю архив проекта ${ZIP_FILE} в директорию ${GRN}${TEMP_DIR}${RST}..."
    mv "$ZIP_FILE" "$TEMP_DIR" || error_exit "Не удалось переместить архив"
    echo -e "${GRN}Перемещено${RST}"
    ;;
esac

echo -e "Устанавливаю разрешения ${GRN}0644${RST} на все файлы в ${GRN}${TEMP_DIR}${RST}..."
find "$TEMP_DIR" -type f -exec chmod 0644 {} + || error_exit "Не удалось установить разрешения"
echo -e "${GRN}Установлено${RST}"

echo -e "Устанавливаю разрешения ${GRN}0755${RST} на все директории в ${GRN}${TEMP_DIR}${RST}..."
find "$TEMP_DIR" -type d -exec chmod 0755 {} + || error_exit "Не удалось установить разрешения"
echo -e "${GRN}Установлено${RST}"

if [ -d "${TEMP_DIR}/${MEDIA_DIR}" ]; then
  echo -e "Меняю владельца директории ${GRN}${TEMP_DIR}/${MEDIA_DIR}${RST} на пользователя ${GRN}${WWW_USER}${RST}..."
  chown -R "$WWW_USER:" "${TEMP_DIR}/${MEDIA_DIR}" || error_exit "Не удалось сменить владельца"
  echo -e "${GRN}Изменён${RST}"
fi

echo -e "Создаю виртуальное окружение ${GRN}${TEMP_DIR}/${VENV_DIR}${RST}..."
python3 -m venv "${TEMP_DIR}/${VENV_DIR}" || error_exit "Не удалось создать виртуальное окружение"
echo -e "${GRN}Создано${RST}"

echo -e "Обновляю ${GRN}pip${RST}..."
"${TEMP_DIR}/${VENV_DIR}/bin/pip" install --upgrade pip -q || error_exit "Не удалось обновить pip"
echo -e "${GRN}Обновлено${RST}"

echo -e "Устанавливаю зависимости из ${GRN}${REQUIREMENTS_FILE}${RST}..."
"${TEMP_DIR}/${VENV_DIR}/bin/pip" install -q -r "${TEMP_DIR}/${REQUIREMENTS_FILE}" || error_exit "Не удалось установить зависимости"
echo -e "${GRN}Зависимости установлены${RST}"

case "${COPY_ENV_FILE,,}" in
  yes|y|true|1)
    echo -e "Копирую файл переменных окружения ${GRN}${PROJECT_DIR}/${ENV_FILE}${RST} в ${GRN}${TEMP_DIR}${RST}..."
    cp "${PROJECT_DIR}/${ENV_FILE}" "$TEMP_DIR" || error_exit "Не удалось скопировать файл"
    echo -e "${GRN}Скопирован${RST}"
    ;;
  *)
    echo -e "${YLW}Пропускаю копирование файла переменных окружения${RST}"
    ;;
esac

if [ -f "${PROJECT_DIR}/${GUNICORN_CONF_FILE}" ]; then
  echo -e "Копирую файл конфигурации gunicorn ${GRN}${PROJECT_DIR}/${GUNICORN_CONF_FILE}${RST} в ${GRN}${TEMP_DIR}${RST}..."
  cp "${PROJECT_DIR}/${GUNICORN_CONF_FILE}" "$TEMP_DIR" || error_exit "Не удалось скопировать файл"
  echo -e "${GRN}Скопирован${RST}"
else
  echo -e "${YLW}Файл конфигурации gunicorn не найден в текущей версии, пропускаю${RST}"
fi


echo -e "\n-----------------------------------------------------------------------"
echo -e "${GRN}Подготовка к обновлению успешно выполнена!${RST}"
echo -e "\nРезервные копии базы данных сохранены в ${GRN}${BACKUP_DIR}/${RST}"
echo -e "\nПроверьте файл настроек ${GRN}settings.py${RST} в директории ${GRN}${TEMP_DIR}/${PROJECT_NAME}${RST}"
echo -e "\nПроверьте файл переменных окружения ${GRN}${ENV_FILE}${RST} в директории ${GRN}${TEMP_DIR}${RST}"
echo -e "\nИ при необходимости отредактируйте их"
echo -e "\nПосле этого запустите процесс обновления, выполнив команду: ${GRN}./update.sh${RST}\n"

exit 0
