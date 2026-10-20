
## Boeren en wolven

**Opgave:**

Er zijn **drie boeren** en **drie wolven** die een rivier moeten oversteken. Ze beschikken over een klein bootje waar telkens **maximaal twee** wezens tegelijk op kunnen.
De **wolven vallen aan** als ze in de meerderheid zijn ten opzichte van de boeren aan **één kant van de rivier** (tenzij daar helemaal geen boeren zijn).
Je moet een plan maken om iedereen **veilig** naar de overkant te brengen, zonder dat de wolven ooit een boer aanvallen.

---

### Spelregels

* Het bootje kan **1 of 2 wezens** tegelijk vervoeren.
* Er moeten altijd wezens in het bootje zitten om het te laten varen. Wolven kunnen evengoed varen.
* Op **geen enkel moment** mag het aantal wolven op een oever **groter zijn dan het aantal boeren**, tenzij er **geen boeren** op die oever zijn.
* Het bootje begint aan de **linkerkant** van de rivier.
* Doel: alle boeren en wolven staan veilig aan de **rechterkant** van de rivier.
* Bijkomend doel: je wil dit liefst doen in zo weinig mogelijk overtochten.

---
### Staat representatie

Een toestand kan worden weergegeven als een tuple van de vorm:

```python
(boeren_links, wolven_links, boot_kant)
```

* `boeren_links`: aantal boeren aan de linkeroever
* `wolven_links`: aantal wolven aan de linkeroever
* `boot_kant`: 0 als het bootje links is, 1 als het rechts is

Voorbeeld beginstaat:

```python
(3, 3, 0)  # alles staat links
```

Voorbeeld met 2 boeren links, 1 boer rechts, 2 wolf links, 1 wolf rechts, boot aan de rechterkant:

```python
(2, 2, 1)  # alles staat rechts
```

---

### Mogelijke overtochten

De boot kan deze combinaties meenemen (beide richtingen):

* (1 boer)
* (2 boeren)
* (1 wolf)
* (2 wolven)
* (1 boer + 1 wolf)

### Puntenverdeling

| Onderdeel               | Punten |
|-------------------------|--------|
| `is_valid_state()`     | 5      |
| `get_new_states()`     | 5      |
| `solve()`               | 5      |
| Doelstaat      | 3      |
| Algoritmekeuze         | 2      |
| **Totaal**             | **20** |


### Bonuspunt
- Maak het aantal boeren en wolven variabel, die je als parameter aan de constructor kan meegeven.