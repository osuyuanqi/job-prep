## [system design intv](https://www.geeksforgeeks.org/5-common-system-design-concepts-for-interview-preparation/)

- vertical scaling-> parallel computing, [exhaust resources.](https://touchstonesecurity.com/horizontal-vs-vertical-scaling-what-you-need-to-know/#:~:text=Scaling%20or%20vertical%20scaling%20is,with%20a%20more%20powerful%20server)
- Horizontal Scaling-> cheap hardware, slower multiple server.
- Return the public IP address of the load balancer, and let the load balancer determin how to actually route data to the backend server (private address).

#### Load Balancing
- A load balancer’s job is to distribute traffic to many different servers to help with throughput, performance, latency, and scalability. You can put the load balancer in front of the clients (it can be also inserted to other places) and then the load balancer will route the incoming request across multiple web servers. In short, load balancers are traffic managers and they take responsibility for the availability and throughput of the system

#### Caching
- Accessing data from primary memory (RAM) is faster than accessing data from secondary memory (disk). By using the caching technique you can speed up the performance of your system. 
- A lot of websites use CDN (content delivery network) which is a global network of servers. CDN caches static assets files like images, javascript, HTML, or CSS and it makes accessing very fast for the users. You can insert caching in on the client (e.g. browser storage), between the client and the server (e.g. CDNs), or on the server itself. 
- memchached: store whatever you want in RAM (garbage collection: expire objects based on when they are put in). *just update.. If multiple times, probably move him from the front line..*

#### Proxies
- In general, when people use the term proxy they refer to ‘forward proxy’. ‘Forward proxy’ is designed to help users and it acts on behalf of (substitute for) the client in the interaction between client and server. 
- ‘Reverse proxies’ are the opposite of ‘forward proxy’. A reverse proxy acts on behalf of a server and it is designed to help servers. 
- A ‘reverse proxy’ can be assigned a lot of tasks to help the main server and it can act as a gatekeeper, a screener, a load-balancer, and an all-around assistant. 

#### CAP Theorem
- distributed system has three significant characteristics: Consistency, Availability, Partition tolerance.
- They can't be existed same time, assume: G1,G2 are servers, client. since:
  - **Partition tolerance** can't be avoided because the information can be transfer errors.
  - [e.g.](https://www.ruanyifeng.com/blog/2018/07/cap.html) when G1 transfer info to G2. If keeps consistency, G2 should be locked and can't be wrote, which means that the availability is not accessble.
- Q: when to choose A over C? e.g. there's a fault in your website->need to update every pages. Though some pages maybe not that latest, they could be updated later.
- You can only pick two out of three at a time and that totally depends on your prioritize based on your requirements. For example, if your system needs to be available and partition tolerant, then you must be willing to accept some latency in your consistency requirements.
- Consistency means that any read request will return the most recent write. Data consistency is usually “strong” for SQL databases and for NoSQL database consistency may be anything from “eventual” to “strong”.
- Availability means that a non-responding node must respond in a reasonable amount of time. Not every application needs to run 24/7 with 99.999% availability but most likely you will prefer a database with higher availability.
- Partition tolerance means the system will continue to operate despite network or node failures.
- Is it actually ok if your system goes down for a few seconds or a few minutes, if not then availability should be your prime concern? If you’re dealing with something with real transactional information like a stock transaction or financial transaction you might value consistency above all. Try to choose the technology that is best suited to the trade-offs that you want to make. 

#### Databases
- Database Indexing: add an index in a table 
- Replication: 
  - What will happen if your database handles so much load? It will be crash at a certain point and your entire system will stop working because all the requests depend on data in the servers. To avoid this kind of failure we use replication which simply means duplicating your database (master) and allow only to read operation on these replicas (slave) of your database. 
  - You can choose synchronous (at the same time as the changes to the main database) or asynchronous approach depending on your needs.
  - Sharding or Data Partitioning:
    - Replication of data solves the availability issue but it doesn’t solve the throughput and latency issues (speed).
    - Take the example of Twitter where a lot of writes are performed. To handle this case you can use database sharding where you split up the database into multiple master databases. 
    - There are mainly two ways to shard your database- horizontal sharding and vertical sharding. 
    - In vertical sharding, each table -> a new machine.
    - horizontal partitioning depends on one key which is an attribute of the data you’re storing to partition data. 
=========

## Storage Scalability 

- Do note that no design is correct or wrong. There are just good designs and bad designs which heavily depend on the use case. 
- UDP is a much faster, simpler, and efficient protocol, however, retransmission of lost data packets is only possible with TCP.
