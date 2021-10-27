import SignUp from "./routes/SignUp";
import SignIn from "./routes/SignIn";
import Home from "./routes/Home";
import Retailer from "./routes/Retailer";
import Wholesaler from "./routes/Wholesaler";
import Distributor from "./routes/Distributor";
import Factory from "./routes/Factory";
import ChooseMode from "./routes/ChooseMode";
import { ThemeProvider } from "@material-ui/core";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Redirect,
} from "react-router-dom";

import "./App.css";
import BeerGameTheme from "./theme/beer_game_theme";

// This is the entry point of the web app.

// The web app uses the 'react-router' package to handle routing.

function App() {
  return (
    <ThemeProvider theme={BeerGameTheme}>
      <Router>
        <div className="App">

          <header className="App-header">
            <p><a href="/home">Beer Game</a></p>
          </header>

          <div className="App-body">
            {/*The <Switch> component renders only the <Route> with the matching URL/path.*/}
            <Switch>
              <Route path="/home">
                <Home />
              </Route>
              <Route path="/signin">
                <SignIn />
              </Route>
              <Route path="/signup">
                <SignUp />
              </Route>
              <Route path="/choosemode">
                <ChooseMode />
              </Route>
              <Route path="/retailer">
                <Retailer />
              </Route>
              <Route path="/distributor">
                <Distributor />
              </Route>
              <Route path="/wholesaler">
                <Wholesaler />
              </Route>
              <Route path="/factory">
                <Factory />
              </Route>
              <Route path="/">
                <Redirect to="/home" />
              </Route>
            </Switch>
          </div>

          <footer className="App-footer">
            <div className="App-footer-content">
              <table className="App-footer-sitemap">
                <tbody>
                  <tr>
                    <td>Site Map</td>
                  </tr>
                  <tr>
                    <td><small><a href="/home">Home</a></small></td>
                  </tr>
                  <tr>
                    <td><small><a href="/signin">Sign In</a></small></td>
                  </tr>
                  <tr>
                    <td><small><a href="/signup">Sign Up</a></small></td>
                  </tr>
                </tbody>
              </table>
              <table className="App-footer-sitemap">
                <tbody>
                  <tr>
                    <td></td>
                  </tr>
                  <tr>
                    <td><small><a href="/retailer">Retailer</a></small></td>
                  </tr>
                  <tr>
                    <td><small><a href="/wholesaler">Wholesaler</a></small></td>
                  </tr>
                  <tr>
                    <td><small><a href="/distributor">Distributor</a></small></td>
                  </tr>
                  <tr>
                    <td><small><a href="/factory">Factory</a></small></td>
                  </tr>
                </tbody>
              </table>
              <table className="App-footer-contact">
                <tbody>
                  <tr>
                    <td><small>Campus Ring 1,<br />28759 Bremen,<br />Jacobs University Bremen (JUB)</small></td>
                  </tr>
                  <tr>
                    <td><small><b>Software Engineering Group 19</b></small></td>
                  </tr>
                </tbody>
              </table>
            </div>

            <small>&copy; Copyright 2021, JUB Beergame SE-Team-19</small>
          </footer>

        </div>
      </Router>
    </ThemeProvider>
  );
}

export default App;
