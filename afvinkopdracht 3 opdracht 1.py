def dict():

    mean_dist = {"io":1821.6,"europe": 1560.8, "ganymede": 2634.1,
                 "callisto":2410.3}
    surface_grav = {"io":1.796, "europe": 1.314, "ganymede": 1.428,
                    "callisto": 1.235}
    orbital_period = {"io": 1.796, "europe":3.551, "ganymede": 7.154,
                        "callisto": 16.689}
    moon = input("please enter a galilean moon")
    moon.lower()


    print(mean_dist[moon])
    print(surface_grav[moon])
    print(orbital_period[moon])


    if moon not in mean_dist:
        print("please enter a different moon")





def main():
    dict()
main()
