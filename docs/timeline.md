## Timeline chart

The timeline chart showcases a single sprint in which this coding excerisse will be implemented. Due to the small size of the task, no more than one week should be spent from start to finish. The timeline can be seen as a high level descripiron of what work needs to be completed in what order. Detail will be kept brief asimplementation plans have been discussed in the relevant ADR's. The points in the timeline could be broken down into several smaller tickets which will complete the timeline event when finished. 

```mermaid
flowchart TB;

1[Prepare relevant documentation]
2[Assemble the folder structure]
3[Begin backend implementation, starting with domain layer and building up towards the entrypoint layer]
4[Write tests for the backend]
5[Containerise the backend]
6[Create the Makefile]
7[Begin Frontend implementation]
8[Write tests for the frontend]
9[QOL improvements, final checks, buffer time]

1 --> 2
2 --> 3
3 --> 4
4 --> 5
5 --> 6
6 --> 7
7 --> 8
8 --> 9
```