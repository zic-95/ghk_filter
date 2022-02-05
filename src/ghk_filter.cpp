#include "ghk_filter.h"
//g filter implementation
g_filter::g_filter(double x_0, double g) : _g(g)
{
    _x_state = x_0;
}

g_filter::~g_filter()
{
}

double g_filter::g_fil_update(double measurement)
{
    double residual = 0;
    residual = measurement - _x_state;
    _x_state = _x_state + _g * (residual);
    return _x_state;
}

//gh filter implementation
gh_filter::gh_filter(double x_0, double dx_0, double g, double h, double dt) : _g(g), _h(h), _dt(dt)
{
    _x_state[0] = x_0;
    _x_state[1] = dx_0;
}

gh_filter::~gh_filter()
{
}

double gh_filter::gh_fil_update(double measurement)
{
    double x_pred, residual = 0;
    //Predict usint state  extrapolation equations for 1st order filter:
    x_pred = _x_state[0] + (_x_state[1] * _dt);
    // We are assuming in state extrapolation that there is no change in "velocity"
    // _x_state[1] = _x_state[1];

    //Update prediction using measurements update:
    residual = measurement - x_pred;
    _x_state[1] = _x_state[1] + _h * (residual / _dt);
    _x_state[0] = x_pred + _g * (residual);

    return _x_state[0];
}

//ghk filter implementation
ghk_filter::ghk_filter(double x_0, double dx_0, double ddx_0, double g, double h, double k, double dt) : _g(g), _h(h), _k(k), _dt(dt)
{
    _x_state[0] = x_0;
    _x_state[1] = dx_0;
    _x_state[2] = ddx_0;
}

ghk_filter::~ghk_filter()
{
}

double ghk_filter::ghk_fil_update(double measurement)
{
    double x_pred, dx_pred, residual = 0;
    //Predict using state  extrapolation equations for 2st order filter:
    x_pred = _x_state[0] + (_x_state[1] * _dt) + (_x_state[2] * _dt * _dt / 2);
    dx_pred = _x_state[1] + _x_state[2] * _dt;
    // We are assuming in state extrapolation that there is no change in "acceleration"
    // _x_state[2] = _x_state[2];

    //Update prediction using measurements update:
    residual = measurement - x_pred;
    _x_state[2] = _x_state[2] + _k * (residual / (0.5 * _dt * _dt));
    _x_state[1] = dx_pred + _h * (residual / _dt);
    _x_state[0] = x_pred + _g * (residual);

    return _x_state[0];
}