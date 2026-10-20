async function chargerAnnonces() {
    try {
        const response = await fetch("http://127.0.0.1:8000/annonces"); //permet de récupérer les données de l'API FastAPI. L'URL "http://

        if (!response.ok) { // Vérifie si la réponse est correcte (code HTTP 200)
            throw new Error(`Erreur HTTP : ${response.status}`);
        }

        const annonces = await response.json(); // Convertit la réponse en JSON pour obtenir les données des annonces

        console.log(annonces); // Affiche les données des annonces dans la console pour le débogage

        const tbody = document.getElementById("annonces-table-body"); // Récupère l'élément <tbody> du tableau HTML où les annonces seront affichées
        console.log(tbody);

        tbody.innerHTML = ""; // Vide le contenu actuel du <tbody> pour éviter d'afficher des annonces en double

        annonces.forEach(annonce => { // Parcourt chaque annonce dans le tableau d'annonces récupéré

            const ligne = document.createElement("tr"); // Crée un nouvel élément <tr> pour chaque annonce afin de représenter une ligne du tableau

            // Remplit la ligne avec les données de l'annonce en utilisant la syntaxe de template string pour insérer les valeurs dans les cellules du tableau
            ligne.innerHTML = `
                <td>${annonce.produit}</td> 
                <td>${annonce.quantite}</td>
                <td>${annonce.ville}</td>
                <td>${annonce.lat}</td>
                <td>${annonce.long}</td>
                <td>${annonce.date}</td>
            `;

            tbody.appendChild(ligne); // Ajoute la ligne créée au <tbody> du tableau pour l'afficher sur la page
        });

    } catch (error) { // Gère les erreurs qui peuvent survenir lors de la récupération des données ou du traitement des annonces
        console.error(error);
    }
}
chargerAnnonces(); // Appelle la fonction chargerAnnonces() pour récupérer et afficher les annonces dès que le script est exécuté
