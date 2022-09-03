def gauss_genetic_optimization(X_data, Y_data):

    N = 50;
    number_of_steps = len(X_data)
    params = 3

    vec, vec2 = list(range(N * params)), list(range(N * params))
    cost, cost2 = list(range(N)), list(range(N))

    # agents initialization
    for i in range(N):
        vec[i] = 5000 + 5000*( random() -0.5)
        vec[i + N] = 5 * random()
        vec[i + 2*N] = 0.1 * random()


    cost = calculate_cost(X_data, Y_data, vec);

    for loop in range(800):
        for j in range(N):
            e = 2 * random() - 1
            z1 = round((N - 1) * random())
            z2 = round((N - 1) * random())
            vec2[j] = vec[j] + e * (vec[z1] - vec[z2])
            vec2[j + N] = vec[j + N] + e * (vec[z1 + N] - vec[z2 + N])
            vec2[j + 2*N] = vec[j + 2*N] + e * (vec[z1 + 2*N] - vec[z2 + 2*N])

            vec2[j] = apply_boundary(0, 25000, vec2[j]);
            vec2[j + N] = apply_boundary(5.25, 5.3, vec2[j + N]);
            vec2[j + 2*N] = apply_boundary(0, 2, vec2[j + 2*N]);

        cost2 = calculate_cost(X_data, Y_data, vec2)

        for j in range(N):
            if cost2[j] < cost[j]:
                vec[j] = vec2[j]
                vec[j + N] = vec2[j + N]
                vec[j + 2*N] = vec2[j + 2*N]
                cost[j] = cost2[j]

    cost2 = calculate_cost(X_data, Y_data, vec)

    best_solution = cost2.index(min(cost2))

    return vec[best_solution], vec[best_solution + N], vec[best_solution + 2*N]


def calculate_cost(X_data, Y_data, agents):
    Calculated_cost = 0
    cost = []
    N = int(len(agents)/3)
    for i in range(N):
        Calculated_cost = 0
        for k in range(len(X_data)):
            Calculated_cost = Calculated_cost + math.pow( gauss(X_data[k], agents[i],
                                agents[i + N], agents[i + 2*N]) - Y_data[k], 2);

        cost.append(Calculated_cost)

    return cost

def apply_boundary(min, max, value):
    result = 0
    if value < min :
        result = min + 0.01 * (max - min) * random()
    elif value > max :
        result = max - 0.01 * (max - min) * random()
    else :
        result = value

    return result
