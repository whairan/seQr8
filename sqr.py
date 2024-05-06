"""

+---------------------+       +----------------------------+       +------------------+
|                     |       |                            |       |                  |
|  Data Collection    +------>+  Processing & Analysis     +------>+  SIEM System     |
|  (Fluentd, Beats)   |       |  (Elasticsearch, Kafka,    |       |  (Elastic Stack) |
|                     |       |   Machine Learning)        |       |                  |
+----------+----------+       +--------------+-------------+       +--------+---------+
           |                                   |                              |
           |                                   |                              |
           |                                   |                              |
           v                                   v                              v
+----------+----------+       +--------------+-------------+       +--------+---------+
|                     |       |                            |       |                  |
|  SOAR Capabilities  |       |  Dashboard & User          |       |  Database        |
|  (StackStorm, NiFi) |       |  Interface (React.js,      |       |  Storage         |
|                     |       |  Chart.js)                 |       |  (PostgreSQL,    |
+---------------------+       +----------------------------+       |   MongoDB)       |
                                                                   |                  |
                                                                   +------------------+


"""