import { Button, Grid, CssBaseline} from '@material-ui/core';
import { makeStyles} from '@material-ui/core/styles';
import React from 'react';
import {Link} from "react-router-dom";

// Returns a map object with css classes, which are applied to Components as css.
const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  root: {
      height: 200,
      display: "flex",
      justifyContent: "center",
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: '100%', // Fix IE 11 issue.
    marginTop: theme.spacing(3),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

export default function Home() {
    const classes = useStyles();
    return (
        <div className={classes.root}>
        <CssBaseline/>
        <Grid container spacing={2} direction="row" alignItems="center" justify="center" height="100%">
            <Grid item>
                <Button variant="contained" color="primary" component={Link} to="/signin">Sign In</Button>
            </Grid>
            <Grid item>
                <Button variant="contained" color="secondary" component={Link} to="/signup">Sign Up</Button>
            </Grid>
        </Grid>
        </div>
    );
}