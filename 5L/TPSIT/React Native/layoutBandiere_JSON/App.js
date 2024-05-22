import React, { useState, useEffect } from 'react';
import { View, ScrollView, Text, StyleSheet, Image, Button, Alert } from 'react-native';
import fetch from 'node-fetch';

const App = () => {
  const [data, setData] = useState([]); // Stato per i dati JSON
  const [isLoading, setIsLoading] = useState(true); // Stato per il caricamento

  useEffect(() => {
    const url = 'https://raw.githubusercontent.com/MattiaBracco05/SCUOLA/main/5L/TPSIT/React%20Native/JSON/Bandiere.json'; // URL del file JSON su GitHub
    fetch(url)
      .then((response) => response.json())
      .then((jsonData) => setData(jsonData))
      .finally(() => setIsLoading(false)); // Imposta isLoading su false al termine del caricamento
  }, []);

  const handleVincitore = (item) => {
    const squadraVincente = item.squadra1.punteggio > item.squadra2.punteggio ? item.squadra1.nomenazione : item.squadra2.nomenazione;
    Alert.alert(`La squadra vincitrice è ${squadraVincente}`);
  };

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerText}>Risultati Partite</Text>
      </View>
      {isLoading ? (
        <Text>Caricamento in corso...</Text>
      ) : (
        <ScrollView showsVerticalScrollIndicator={true}>
          {data.map((item, index) => (
            
            <View key={index} style={styles.match}>
              <Text style={styles.matchTitle}>{item.squadra1.nomenazione} VS {item.squadra2.nomenazione}</Text>
              <Button title="Vincitore" onPress={() => handleVincitore(item)} style={styles.teamScore} />

              <View style={styles.team}>
                <Image style={styles.immagine} source={{ uri: item.squadra1.immagine }} />
                <Text style={styles.teamScore}>{item.squadra1.punteggio}</Text>
              </View>
              
              <View style={styles.team}>
                <Image style={styles.immagine} source={{ uri: item.squadra2.immagine }} />
                <Text style={styles.teamScore}>{item.squadra2.punteggio}</Text>
              </View>
            
            </View>
          ))}
        </ScrollView>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  header: {
    backgroundColor: '#f0f0f0',
    padding: 20,
  },
  headerText: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  match: {
    padding: 20,
    borderBottomWidth: 1,
    borderColor: '#ccc',
  },
  matchTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  team: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 10,
  },
  immagine: {
    width: 50,
    height: 30,
    marginRight: 10,
  },
  teamScore: {
    fontSize: 30,
    textAlign: 'right',
    flex: 1,
    marginRight: 10,
    marginBottom: 10, // Margine in basso
  },
});

export default App;