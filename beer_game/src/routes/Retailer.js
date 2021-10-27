import React, { useState } from 'react';
import { Button, CssBaseline, TextField, Typography, Container } from "@material-ui/core";
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import axios from 'axios';
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
    table: {
        minWidth: 700,
        // margin: 50
    },
    submit: {
        margin: theme.spacing(3, 0, 2),
    },
}));



export default function SpanningTable() {
    const classes = useStyles();
    const [outgoing_order, setOutgoingOrder] = useState();
    const handleSubmit = (evt) => {
        evt.preventDefault();
        axios.get(`http://localhost:5000/1/make_retailer_order?outgoing=${outgoing_order}`)
        .then(function (response) {
            // handle success
            console.log(response);
            setOutgoing (response.data.outgoing);
            setStock (response.data.inventory);
            setBacklog (response.data.backorder);
            setIncoming (response.data.incoming);
          })
          .catch(function (error) {
            // handle error
                alert(`${error}`);
          })
          .then(function () {
            // always executed
          });
    }

    const [outgoing, setOutgoing] = useState (0);
    const [stock, setStock] = useState (0);
    const [backlog, setBacklog] = useState (0);
    const [incoming, setIncoming] = useState (0);

    return (
        <Container component="main" maxWidth="lg">
            <CssBaseline />
            <div className={classes.paper}>
                <Typography component="h1" variant="h5">
                    Retailer
        </Typography>
                <br></br>
                <form className={classes.form} onSubmit={handleSubmit}>
                <TableContainer component={Paper}>
                    <Table className={classes.table} aria-label="spanning table">
                        <TableBody>
                            <TableRow>
                                <TableCell>
                                    <TextField
                                        variant="filled"
                                        disabled
                                        id="incoming_order"
                                        label="Incoming Order"
                                        name="incoming_order"
                                        autoComplete="incoming_order"
                                        autoFocus
                                    />
                                </TableCell>
                                <TableCell> 
                                <TextField
                                        variant="filled"
                                        disabled
                                        id="stock"
                                        label="Stock"
                                        name="stock"
                                        value= {stock}
                                        autoComplete="stock"
                                        autoFocus
                                    />
                                </TableCell>
                                <TableCell> -------------- </TableCell>
                                <TableCell>
                                <TextField
                                        variant="filled"
                                        disabled
                                        id="outgoing"
                                        label="Outgoing"
                                        name="outgoing"
                                        value= {outgoing}
                                        autoComplete="outgoing"
                                        autoFocus
                                    />
                                </TableCell>
                            </TableRow>
                            <TableRow>
                                <TableCell>
                                    <TextField
                                    variant="outlined"
                                    required
                                    id="outgoing_order"
                                    label="Outgoing Order"
                                    name="outgoing_order"
                                    autoComplete="outgoing_order"
                                    autoFocus
                                    onChange={e => setOutgoingOrder(e.target.value)}
                                /> 
                                </TableCell>
                                <TableCell>
                                <TextField
                                        variant="filled"
                                        disabled
                                        id="backlog"
                                        label="Backlog"
                                        name="backlog"
                                        value= {backlog}
                                        autoComplete="backlog"
                                        autoFocus
                                    />
                                     </TableCell>
                                <TableCell> &larr;&larr;&larr;&larr;&larr; </TableCell>
                                <TableCell>
                                <TextField
                                        variant="filled"
                                        disabled
                                        id="incoming"
                                        label="Incoming next week"
                                        name="incoming"
                                        value= {incoming}
                                        autoComplete="incoming"
                                        autoFocus
                                    />
                                </TableCell>
                            </TableRow>
                            <TableRow>
                                <TableCell rowSpan={3} />
                                <TableCell colSpan={2}></TableCell>
                                <TableCell align="right">
                                <Button variant="contained" color="secondary" type="submit" aria-label="goButton" >Go</Button>
                                </TableCell>
                            </TableRow>
                        </TableBody>
                    </Table>
                </TableContainer>
                </form>
            </div>
        </Container>
    );
}
