#!/bin/bash

# Variables
GIT_EMAIL="aminebenmahdi@ecole2600.com"
GIT_NAME="aminebenmahdi"
REPO_URL="git@github.com:aminebenmahdi/turin.git"

# Initialiser le dépôt
echo "Initialisation du dépôt Git..."
git init

# Configurer les informations de l'utilisateur Git
git config user.name "$GIT_NAME"
git config user.email "$GIT_EMAIL"

# Ajouter le dépôt distant
echo "Configuration du dépôt distant..."
git remote add origin "$REPO_URL"

# Ajouter tous les fichiers
echo "Ajout des fichiers au dépôt..."
git add .

# Commit initial
echo "Création du commit initial..."
git commit -m "Initial commit"

# Pousser les modifications
echo "Pousser les modifications vers le dépôt distant..."
git push -u origin main

echo "Configuration terminée !"
