import React from 'react';
import { Route } from 'react-router-dom';

import MainPage from './containers/MainPage';
import Login from './containers/Login';
import Signup from './containers/Signup';

const BaseRouter = () => {
    return (
        <div>
            <Route exact path="/" component={MainPage} />{" "}
            <Route exact path="/login" component={Login} />{" "}
            <Route exact path="/signup" component={Signup} />{" "}
        </div>
    )
}

export default BaseRouter;
