#!/bin/bash

# Поиск файлов содержащих "BattleOfTheBots" (без учета регистра)
echo "Searching for files containing 'BattleOfTheBots':"
find . -type f -exec grep -il "TheBattleOfTheBots" {} \;

# Поиск файлов содержащих "Битва Ботов" (без учета регистра)
echo -e "\nSearching for files containing 'Битва Ботов':"
find . -type f -exec grep -il "Битв* Ботов" {} \;