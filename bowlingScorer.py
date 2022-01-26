def list_sum(list):
    sum = 0
    for score in list:
        sum = sum + score
        
    return sum

def calc_score(score_list):
    total_sum = 0
    for key, list in score_list.items():

        if len(list) == 0:
            break
            
        print("%d프레임 점수 : %d" % (key, list_sum(list)))
        total_sum = total_sum + list_sum(list)
    
    print('총 점수 :', total_sum)
    
def get_input(frame, tryCount):
    pin_count = int(input('{}프레임 {}차 시도 핀 개수를 입력하세요 : '.format(frame, tryCount)))
    
    if pin_count < 0 or 10 < pin_count:
        print("올바른 핀 개수를 입력해주세요")
        
        while True:
            pin_count = int(input('{}프레임 {}차 시도 핀 개수를 입력하세요 : '.format(frame, tryCount)))
            
            if pin_count < 0 or 10 < pin_count:
                print("올바른 핀 개수를 입력해주세요")
            else:
                break
            
    return pin_count

def release_ball(score_list, frame, pin_strike):
    
    g_strike = 10
    g_lastFrame = 10
    
    score_list[frame].append(pin_strike)
    
    if 1 < frame:
        if len(score_list[frame - 1]) == 1: ## 이전 프레임이 스트라이크
            score_list[frame - 1][0] += pin_strike
            
        if len(score_list[frame - 1]) == 2: ## 이전 프레임이 스트라이크 아님
            first = score_list[frame - 1][0]
            second = score_list[frame - 1][1]

            if first + second == g_strike:
                score_list[frame - 1][1] += pin_strike
            
        if 2 < frame and len(score_list[frame - 2]) == 1: ## 이전전 프레임이 스트라이크
            score_list[frame - 2][0] += pin_strike
            
        if pin_strike < g_strike:
            pin_strike = get_input(frame, 2)
            score_list[frame].append(pin_strike)
            
            if len(score_list[frame - 1]) == 1:
                score_list[frame - 1][0] += pin_strike
            
        if frame == g_lastFrame and pin_strike == g_strike:
            pin_strike = get_input(frame, 2)
            score_list[frame].append(pin_strike)
            
            score_list[frame - 1][0] += pin_strike

            pin_strike = get_input(frame, 3)
            score_list[frame].append(pin_strike)
    else:
        if pin_strike < g_strike:
            pin_strike = get_input(frame, 2)
            score_list[frame].append(pin_strike)

if __name__ == "__main__":
    frame = 1
    score_list = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[]}
    
    for data in score_list:
        release_ball(score_list, frame, get_input(frame, 1))
        calc_score(score_list)
        
        frame = frame + 1