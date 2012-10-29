//
//  ReminderMasterViewController.h
//  Reminder
//
//  Created by Администратор on 10/29/12.
//  Copyright (c) 2012 Администратор. All rights reserved.
//

#import <UIKit/UIKit.h>

@class ReminderDetailViewController;

@interface ReminderMasterViewController : UITableViewController

@property (strong, nonatomic) ReminderDetailViewController *detailViewController;

@end
