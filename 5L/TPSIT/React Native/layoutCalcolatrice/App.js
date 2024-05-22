import { StyleSheet, Text, View,Button } from 'react-native'
import React from 'react'

const App = () => {
  return (
    <View style={styles.contenitore}>
      <Text style={styles.casellaTesto}>RISULTATO</Text>
      <View style={styles.riga}>
         <View style={styles.mioView}><Button title='7' /></View>
         <View style={styles.mioView}><Button title='8' /></View>
         <View style={styles.mioView}><Button title='9' /></View>
         <View style={styles.mioView}><Button title='X' /></View>
      </View>
      <View style={styles.riga}>
         <View style={styles.mioView}><Button title='4' /></View>
         <View style={styles.mioView}><Button title='5' /></View>
         <View style={styles.mioView}><Button title='6' /></View>
         <View style={styles.mioView}><Button title='-' /></View>
      </View>
      <View style={styles.riga}>
         <View style={styles.mioView}><Button title='1' /></View>
         <View style={styles.mioView}><Button title='2' /></View>
         <View style={styles.mioView}><Button title='3' /></View>
         <View style={styles.mioView}><Button title='+' /></View>
      </View>
      <View style={styles.riga}>
         <View style={styles.mioView}><Button title='0' /></View>
         <View style={styles.mioView}><Button title='=' /></View>

      </View>
    </View>
  )
}

export default App

const styles = StyleSheet.create({
  casellaTesto:{
    backgroundColor:"red",
    height:100,
    width:400,
    textAlign:"center",
    color:"white",
    fontSize:30
  },
  riga:{
    display:"flex",
    flexDirection:"row",
    justifyContent:"center"
  },
  mioView:{
    width:100
  }
})