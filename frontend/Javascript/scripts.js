async function chargerAnnonces() {

    const tbody = document.getElementById("annonces-table-body"); 

    //Utile parce que j utilise le meme script pour publier et afficher les annonces. 
    // Si je suis sur la page publier.html, il n y a pas de tbody, ca va me generer une erreur. Je verifie  si le tbody existe avant de continuer.
    if (!tbody) { // Vérifie si l'élément <tbody> existe dans le DOM avant de continuer. Si l'élément n'existe pas, la fonction s'arrête pour éviter des erreurs.
        return;
    }

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
console.log("scripts.js chargé");

async function publierAnnonce(event) {

    event.preventDefault(); // Empêche le comportement par défaut du formulaire (rechargement de la page) lors de la soumission

     console.log("Étape 1"); // Affiche un message dans la console pour indiquer que la fonction publierAnnonce a été appelée

    // Récupère les valeurs des champs du formulaire et les stocke dans un objet annonce. 
    // Les valeurs sont converties en types appropriés (Number pour quantite, lat et long)
    const annonce = {
        produit: document.getElementById("nom").value,
        quantite: Number(document.getElementById("quantite").value),
        ville: document.getElementById("ville").value,
        lat: Number(document.getElementById("latitude").value),
        long: Number(document.getElementById("longitude").value),
        date: document.getElementById("date").value
    };

    console.log("Étape 2",annonce);
    
    // Envoie une requête POST à l'API FastAPI pour publier l'annonce. 
    // La requête inclut les en-têtes nécessaires et le corps de la requête est l'objet annonce converti en JSON.
    const response = await fetch("http://127.0.0.1:8000/annonces",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(annonce) //stingify permet de convertir l'objet JavaScript en une chaîne JSON pour l'envoyer dans le corps de la requête
        }
    );

    // Vérifie si la réponse de l'API est correcte (code HTTP 200) et affiche un message approprié à l'utilisateur.
    if (response.status === 200) { 
        const form = document.getElementById("form-annonce");
        console.log(form);
        form.reset();
        alert("Annonce publiée avec succès !");
    } else {
        alert("Erreur lors de la publication de l'annonce.");
    }

    console.log("Étape 3");

    console.log(response.status);

    // Récupère la réponse de l'API en JSON pour obtenir les détails de l'annonce publiée et les affiche dans la console pour le débogage.
    const resultat = await response.json();

    console.log("Étape 4", resultat);
}

chargerAnnonces(); // Appelle la fonction chargerAnnonces() pour récupérer et afficher les annonces dès que le script est exécuté

// Récupère l'élément du formulaire avec l'ID "form-annonce" pour ajouter un événement de soumission.
const form = document.getElementById("form-annonce"); 

    console.log(form);
    // Vérifie si le formulaire existe avant d'ajouter l'événement de soumission. 
    // Cela évite les erreurs si le script est exécuté sur une page qui n'a pas de formulaire.
    if (form) {
        form.addEventListener("submit", publierAnnonce);
    }
