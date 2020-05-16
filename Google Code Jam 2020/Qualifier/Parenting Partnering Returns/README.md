### [Parenting Partnering Returns](https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9)

### Description

Before sorting the activities, save their order because the order will be used to format output. Then, sort the activities by their start time. Choose either partner for the first activity. Then,

1. For subsequent activity, if the start time is after the end time of current activity, the current partner can perform that activity.
2. If the start time  of next activity is smaller than end time of current activity, then:
     - If no partner switch has happened, the current activity is assigned to second partner. This also implies that previous activity was the activity in progress by partner before switch.
     - If partner switch is necessary and the second partner's activity is still in progress, then the output is IMPOSSIBLE.

3. Once all activities have been parsed, sort the outputs by the original activities indices.