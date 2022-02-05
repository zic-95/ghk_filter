#ifndef GHK_FILTER
#define GHK_FILTER

class g_filter
{
public:
    g_filter(double x_0, double g);
    ~g_filter();
    double g_fil_update(double measurement);

private:
    double _x_state = 0.0;
    double _g = 0.0;
};

class gh_filter
{
public:
    gh_filter(double x_0, double dx_0, double g, double h, double dt);
    ~gh_filter();
    double gh_fil_update(double measurement);

private:
    double _x_state[2] = {0.0, 0.0};
    double _g, _h = 0.0;
    double _dt = 0.0;
};

class ghk_filter
{
public:
    ghk_filter(double x_0, double dx_0, double ddx_0, double g, double h, double k, double dt);
    ~ghk_filter();
    double ghk_fil_update(double measurement);

private:
    double _x_state[3] = {0.0, 0.0, 0.0};
    double _g, _h, _k = 0.0;
    double _dt = 0.0;
};

#endif