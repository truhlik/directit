export const timeSince = (previous, current) => {

    if(!current) current = new Date();

    const msPerMinute = 60 * 1000;
    const msPerHour = msPerMinute * 60;
    const msPerDay = msPerHour * 24;
    const msPerMonth = msPerDay * 30;
    const msPerYear = msPerDay * 365;

    const elapsed = current - previous;

    if (elapsed < msPerMinute) {
        //return Math.round(elapsed/1000) + ' seconds ago';
        return {
            number: Math.round(elapsed/1000),
            type: 'seconds',
        };
    }

    else if (elapsed < msPerHour) {
        //return Math.round(elapsed/msPerMinute) + ' minutes ago';
        return {
            number: Math.round(elapsed/msPerMinute),
            type: 'minutes',
        };
    }

    else if (elapsed < msPerDay ) {
        //return Math.round(elapsed/msPerHour ) + ' hours ago';
        return {
            number: Math.round(elapsed/msPerHour),
            type: 'hours',
        };
    }

    else if (elapsed < msPerMonth) {
        //return 'approximately ' + Math.round(elapsed/msPerDay) + ' days ago';
        return {
            number: Math.round(elapsed/msPerDay),
            type: 'days',
        };
    }

    else if (elapsed < msPerYear) {
        //return 'approximately ' + Math.round(elapsed/msPerMonth) + ' months ago';
        return {
            number: Math.round(elapsed/msPerMonth),
            type: 'months',
        };
    }

    else {
        //return 'approximately ' + Math.round(elapsed/msPerYear ) + ' years ago';
        return {
            number: Math.round(elapsed/msPerYear),
            type: 'years',
        };
    }

}

/*
var aDay = 24*60*60*1000;
console.log(timeSince(new Date(Date.now()-aDay)));
console.log(timeSince(new Date(Date.now()-aDay*2)));*/
