#include <Arduino.h>
#include <ghk_filter.h>

double x0_init = 50;
double dx0_init = 1;
double g_val = 0.75;
double h_val = 0.5;
double dt = 0.1; //s

double g_fil_msr = 0;
double gh_fil_msr = 0;

//init filters
g_filter gFIL(x0_init, g_val);
gh_filter ghFIL(x0_init, dx0_init, g_val, h_val, dt);

unsigned long prev_update_time;
static uint32_t tTime;

void setup()
{
    //setup
}
void loop()
{
    uint32_t t = millis();
    if ((t - tTime) * 10e6 >= dt)
    {
        double msr = 0; //get measurements
        //get filtered values
        g_fil_msr = gFIL.g_fil_update(msr);
        gh_fil_msr = ghFIL.gh_fil_update(msr);

        Serial.print("Raw val: ");
        Serial.print(msr);
        Serial.print(" mm\t");
        Serial.print("G_fil val: ");
        Serial.print(g_fil_msr);
        Serial.print(" mm\t");
        Serial.print("GH_fil val: ");
        Serial.print(gh_fil_msr);
        Serial.print(" mm\n");
        tTime = t;
    }
}
