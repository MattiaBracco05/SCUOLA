import {useEffect, useState} from "react";
import './App.css';
import axios from 'axios';

function App() {
    const CLIENT_ID = "46c318244df94bcbb67ef86ce832ee2c"
    const REDIRECT_URI = "http://localhost:3000"
    const AUTH_ENDPOINT = "https://accounts.spotify.com/authorize"
    const RESPONSE_TYPE = "token"

    const [token, setToken] = useState("")
    const [searchKey, setSearchKey] = useState("")
    const [artists, setArtists] = useState([])

    useEffect(() => {
        const hash = window.location.hash
        let token = window.localStorage.getItem("token")

        if (!token && hash) {
            token = hash.substring(1).split("&").find(elem => elem.startsWith("access_token")).split("=")[1]
            window.location.hash = ""
            window.localStorage.setItem("token", token)
        }

        setToken(token)

    }, [])

    //LOGOUT --> disconnette e rimanda alla pagina di accesso
    const logout = () => {
        setToken("")
        window.localStorage.removeItem("token")
    }

    //CERCA ARTISTA --> richiama l'API per la ricerca
    const cercaArtista = async (e) => {
        e.preventDefault()
        const {data} = await axios.get("https://api.spotify.com/v1/search", {
            headers: {
                Authorization: `Bearer ${token}`
            },
            params: {
                q: searchKey,
                type: "artist"
            }
        })

        setArtists(data.artists.items)
    }

    //MOSTRA ARTISTA --> informazioni
    const mostraArtista = () => {
        return artists.map(artist => (
            <div className='row'>
            {/* immagine */}
            <div class="datiArtista">{artist.images.length ? <img width={"100%"} src={artist.images[0].url} alt=""/> : <div class="col-12">No image<i class="fa fa-sort-amount-desc" aria-hidden="true"></i></div>}</div>
            {/* nome */}
            <div class="col-4 datiArtista">Artista: {artist.name}</div>
        </div>
        ))
    }

    //RETURN --> STAMPA A VIDEO
    return (
        <div className="App">
            <header className="App-header">
                {/* titolo */}
                <h1>React JS ~ Spotify Cover Search</h1>

                {/* BUTTON PER IL LOGUT */}
                {!token ?
                    <a href={`${AUTH_ENDPOINT}?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&response_type=${RESPONSE_TYPE}`}>Login to Spotify</a>
                    : <button className="buttonLogout" onClick={logout}>LOGOUT</button>}

                {/* INPUT PER LA RICERCA */}
                {token ?
                    <form onSubmit={cercaArtista}>
                        {/* casella di testo */}
                        <input type="text" className="textCerca" onChange={e => setSearchKey(e.target.value)}/>
                        {/* button */}
                        <button type={"submit"} className="buttonSearch" >SEARCH</button>
                    </form>
                    : <h2>EFFETTUARE IL LOGIN</h2>
                }

                {mostraArtista()}

            </header>
        </div>
    );
}

export default App;
