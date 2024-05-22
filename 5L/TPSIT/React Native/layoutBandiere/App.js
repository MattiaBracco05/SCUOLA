import React from 'react';
import { View, ScrollView, Text, StyleSheet, Image, Button, Alert } from 'react-native';

const match = [
  {
    squadra1: {
      immagine: "https://flagpedia.net/data/flags/h80/it.png",
      nomenazione: "Italia",
      punteggio: 3
    },
    squadra2: {
      immagine: "https://flagpedia.net/data/flags/h80/fr.png",
      nomenazione: "Francia",
      punteggio: 2
    }
  },
  {
    squadra1: {
      immagine: "https://flagpedia.net/data/flags/h80/de.png",
      nomenazione: "Germania",
      punteggio: 1
    },
    squadra2: {
      immagine: "https://flagpedia.net/data/flags/h80/es.png",
      nomenazione: "Spagna",
      punteggio: 1
    }
  },
  {
    squadra1: {
      immagine: "https://flagpedia.net/data/flags/h80/gb.png",
      nomenazione: "Inghilterra",
      punteggio: 0
    },
    squadra2: {
      immagine: "https://flagpedia.net/data/flags/h80/br.png",
      nomenazione: "Brasile",
      punteggio: 2
    }
  },
  {
    squadra1: {
      immagine: "https://flagpedia.net/data/flags/h80/ar.png",
      nomenazione: "Argentina",
      punteggio: 4
    },
    squadra2: {
      immagine: "https://flagpedia.net/data/flags/h80/pt.png",
      nomenazione: "Portogallo",
      punteggio: 3
    }
  },
  {
    squadra1: {
      immagine: "https://flagpedia.net/data/flags/h80/us.png",
      nomenazione: "Stati Uniti",
      punteggio: 1
    },
    squadra2: {
      immagine: "https://flagpedia.net/data/flags/h80/mx.png",
      nomenazione: "Messico",
      punteggio: 3
    }
  }
];

const App = () => {
  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerText}>Risultati Partite</Text>
      </View>
      
      {/* ScrollView in modo che con tanti match posso scorrerli */}
      <ScrollView showsVerticalScrollIndicator={true}>
      {match.map((item, index) => (
        //Per ogni match...
        
        <View key={index} style={styles.match}>
          {/* Match (Squadra1 vs Squadra2) */}
          <Text style={styles.matchTitle}>{item.squadra1.nomenazione} VS {item.squadra2.nomenazione}</Text>
          <Button title="Scopri il vincitore" onPress={() => handleVincitore(item)} />

          {/* Squadra 1 */}
          <View style={styles.team}>
            <Image style={styles.immagine} source={{uri:item.squadra1.immagine}}/>
            <Text style={styles.teamScore}>{item.squadra1.punteggio}</Text>
          </View>
          
          {/* Squadra 2 */}
          <View style={styles.team}>
            <Image style={styles.immagine} source={{uri:item.squadra2.immagine}}/>
            <Text style={styles.teamScore}>{item.squadra2.punteggio}</Text>
          </View>

        </View>
      ))}
      </ScrollView>

    </View>
  );
};

const handleVincitore = (item) => {
  const squadraVincente = item.squadra1.punteggio > item.squadra2.punteggio ? item.squadra1.nomenazione : item.squadra2.nomenazione;
  Alert.alert(`La squadra vincitrice è ${squadraVincente}`);
};

const styles = StyleSheet.create({
  //CSS generale
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  header: {
    backgroundColor: '#f0f0f0',
    padding: 16,
  },
  headerText: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
  },

  //CSS per il match
  match: {
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#ccc',
  },
  matchTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 8,
  },
  team: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    marginBottom: 8,
    marginTop: 8,
  },
  teamName: {
    fontSize: 18,
    fontWeight: 'bold',
    flex: 1,
  },
  teamScore: {
    fontSize: 30,
    textAlign: 'right',
    flex: 1,
  },

  //CSS per le immagini
  immagine: {
    //Per vedere le immagini devo inserire sia il parametro width che height
    width: 70,
    height: 50,
  }
});

export default App;
