class Tello:
    def __init__(self, actions):
        self.en_vol = False
        self.camera_etat = False
        self.est_en_enregistrement = False
        self.last_action = "Initialisé"
        self.actions = actions  # Référence vers la variable globale actions
        self.actions["last_action"] = "Drone connecté (mode simulé)."
        print(self.actions["last_action"])

    def _update_action(self, action):
        self.last_action = action
        self.actions["last_action"] = action  # Mise à jour globale

    def takeoff(self):
        if not self.en_vol:
            self._update_action("Décollage")
            self.en_vol = True
        else:
            self._update_action("Atterrissage")
            self.en_vol = False
        print(self.last_action)

    def move_up(self):
        if self.en_vol:
            self._update_action("Monte")
            print("Drone monte.")

    def move_down(self):
        if self.en_vol:
            self._update_action("Descend")
            print("Drone descend.")

    def move_left(self):
        if self.en_vol:
            self._update_action("Va à gauche")
            print("Drone va à gauche.")

    def move_right(self):
        if self.en_vol:
            self._update_action("Va à droite")
            print("Drone va à droite.")

    def camera(self):
        if not self.camera_etat:
            self._update_action("Caméra allumée")
            self.camera_etat = True
        else:
            self._update_action("Caméra éteinte")
            self.camera_etat = False
            self.est_en_enregistrement = False
        print(self.last_action)

    def toggle_enregistrement(self):
        if self.camera_etat and not self.est_en_enregistrement:
            self._update_action("Enregistrement démarré")
            self.est_en_enregistrement = True
        elif self.camera_etat and self.est_en_enregistrement:
            self._update_action("Enregistrement arrêté")
            self.est_en_enregistrement = False
        elif not self.camera_etat:
            self._update_action("Impossible d'enregistrer: caméra éteinte")
            self.est_en_enregistrement = False
        print(self.last_action)
