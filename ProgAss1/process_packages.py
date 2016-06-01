# python3


class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time


class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []
        self.done = 0

    def Process(self, request):
        a = len(self.finish_time_)
        if a > 0:
            while request.arrival_time >= self.finish_time_[self.done]:
                self.done += 1
                if self.done == a:
                    break
            if a - self.done > size:
                return Response(True, -1)
            else:
                self.finish_time_.append(request.process_time + max([self.finish_time_[a - 1], request.arrival_time]))
        else:
            self.finish_time_.append(request.process_time + request.arrival_time)
        return Response(False, self.finish_time_[a]-request.process_time)


def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests


def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses


def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
