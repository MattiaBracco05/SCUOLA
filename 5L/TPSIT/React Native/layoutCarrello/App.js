import { StatusBar } from 'expo-status-bar';
import React,{useState} from 'react';
import { StyleSheet,Image,FlatList, Switch, Text, View,Modal, Button, TextInput, TouchableOpacity, Alert } from 'react-native';

export default function App() {

  //Dichiarazione degli useState
  const [visualizza, setVisualizza] = useState(false)
  const [mioTesto, setMioTesto] = useState("")
  const [visualizzaImg, setVisualizzaImg] = useState(false)
  
  //Array di object literal con gli utenti
  const alunni = [
    {
        nome:"andrea",
        cognome:"rossi",
        eta:22
    },
    {
        nome:"paolo",
        cognome:"verdi",
        eta:23
    },
    {
        nome:"simone",
        cognome:"blu",
        eta:24
    },
    {
        nome:"Luca",
        cognome:"nero",
        eta:25
    },
    {
        nome:"Giovanni",
        cognome:"grigio",
        eta:26
    },
    {
        nome:"Antonio",
        cognome:"viola",
        eta:27
    },
    {
        nome:"Lucas",
        cognome:"marrone",
        eta:28
    },
    {
        nome:"Enrico",
        cognome:"rosa",
        eta:29
    },
    {
        nome:"Simona",
        cognome:"arancione",
        eta:30
    },
    {
        nome:"Rocio",
        cognome:"violetta",
        eta:31
    }

  ];

  //Show
  const show = () => {
    setVisualizza(!visualizza)
  }

  //caricaTesto
  const caricaTesto = (testo) => {
    setMioTesto(testo)
  }

  //Modifica (visualizza pc)
  const modifica = () => {
    setVisualizzaImg(!visualizzaImg)
  }

  //Premi (alert con il nome)
  const premi = (utente) => {
    Alert.alert(utente.item.nome)
  }

  //Singola opzione (lista degli utenti)
  const singolaOpzione = (arrayAlunni) => {
    
    //Return --> Ciò che visualizzo a video 
    return (
      
      //Inizio della TouchableOpacity
      <TouchableOpacity onPress={()=>premi(arrayAlunni)}>
        
        {/* Inizio dela View */}
        <View style={styles.singolaopz}>
          {/* Text per il nome */}
          <Text>{arrayAlunni.item.nome}</Text>
          {/* Text per il cognome */}
          <Text>{arrayAlunni.item.cognome}</Text>
          {/* Text per l'età */}
          <Text>{arrayAlunni.item.eta}</Text>
        </View>
        {/* Fine della View */}

    </TouchableOpacity>
    //FIne della TouchableOpacity
    )

  }
  return (
    <View style={styles.container}>
      {/* Text */}
      <Text>MIO CARRELLO</Text>
      
      {/* Button */}
      <Button title="VISUALIZZA CARRELLO" onPress={show} />
      
      {/* Status bar */}
      <StatusBar style="auto" hidden={false}  backgroundColor='yellow'/>
    
    {/* Inizio finestra modale */}
    <Modal visible={visualizza}>
      {/* Text */}
      <Text>FINESTRA MODALE</Text>
      
      {/* Text input */}
      <TextInput style={styles.casellaTesto} onChangeText={caricaTesto} />
     
      {/* Text */}
      <Text>{mioTesto}</Text>
      
      {/* Button */}
      <Button title='PROVA' />
      
      {/* Switch */}
      <Switch value={visualizzaImg} onChange={modifica}/>

        {/* Immagine (che controllo con switch) */}
        {visualizzaImg == true && (<Image style={styles.immagine} source={{uri:"https://www.cartadaparati.com/media/catalog/product/cache/5b18b93ddbe5d6592c6b175f41d24454/a/d/adobestock_290425327-small.jpg"}}/>) }
            
            {/* Flat list */}
            <FlatList
              data = {alunni}
              renderItem = {singolaOpzione}
              keyExtractor = { (item, index) => index.toString() }
            />

    </Modal>
    {/* Fine finestra modale */}
   
    </View>
  );
}

//Style (tipo il CSS)
const styles = StyleSheet.create({
  
  //Conatiner
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },

  //Casella di testo
  casellaTesto:{
    backgroundColor:"yellow",
    width:200,
    height:200,
    borderStyle:"solid",
    borderWidth:1,
    borderColor:"red"
  },

  //Immagine
  immagine:{
    //Per vedere le immagini devo inserire sia il parametro width che height
    width:100,
    height:100
  },

  //SingolaOpz
  singolaopz:{
    borderStyle:"solid",
    borderWidth:1,
    borderColor:"red"
  }
});