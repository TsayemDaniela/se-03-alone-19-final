import {multiply, makeLowerCase} from "./HelperFunctions";
import {render, fireEvent} from "@testing-library/react";

import Home from "../routes/Home";
import SignUp from "../routes/SignUp";
import SignIn from "../routes/SignIn";
import Retailer from "../routes/Retailer";
import Wholesaler from "../routes/Wholesaler";
import Distributor from "../routes/Distributor";
import Factory from "../routes/Factory";
import ChooseMode from "../routes/ChooseMode";

test("defaultChecker", () => {
    expect(multiply(2,10)). toBe(20)
});

it ("checkHomeRender", () => {
    expect (Home).toBeTruthy();
});

it ("checkSignUpRender", () => {
    expect (SignUp).toBeTruthy();
});

it ("checkSignInRender", () => {
    expect (SignIn).toBeTruthy();
});

it ("checkRetailerRender", () => {
    expect (Retailer).toBeTruthy();
});

it ("checkRetailerGoButton", () => {
    const { getByRole } = render(<Retailer />);
    const gobtn = getByRole('button', { name: /goButton/i});
    expect (gobtn).toBeTruthy();
});

it ("checkWholesalerRender", () => {
    expect (Wholesaler).toBeTruthy();
});

it ("checkWholesalerGoButton", () => {
    const { getByRole } = render(<Wholesaler />);
    const gobtn = getByRole('button', { name: /goButton/i});
    expect (gobtn).toBeTruthy();
});

it ("checkDistributorRender", () => {
    expect (Distributor).toBeTruthy();
});

it ("checkDistributerrGoButton", () => {
    const { getByRole } = render(<Distributor />);
    const gobtn = getByRole('button', { name: /goButton/i});
    expect (gobtn).toBeTruthy();
});

it ("checkFactoryRender", () => {
    expect (Factory).toBeTruthy();
});

it ("checkFactoryGoButton", () => {
    const { getByRole } = render(<Factory />);
    const gobtn = getByRole('button', { name: /goButton/i});
    expect (gobtn).toBeTruthy();
});

it ("checkChooseModeRender", () => {
    expect (ChooseMode).toBeTruthy();
});