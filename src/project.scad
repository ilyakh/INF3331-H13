

union() {
	union() {
		union() {
			union() {
				union() {
					translate(v = [15.0000000000, 20.0000000000, 0.0000000000]) {
						mirror(v = [1, 0, 0]) {
							translate(v = [-15.0000000000, -20.0000000000, -0.0000000000]) {
								color(c = "mediumvioletred") {
									translate(v = [15, 20, 0]) {
										difference() {
											union() {
												difference() {
													color(c = "steelblue") {
														translate(v = [0, 0, 0.5000000000]) {
															cube(center = true, size = [10, 10, 1]);
														}
													}
													translate(v = [0.0000000000, 2.5000000000, 0.0000000000]) {
														translate(v = [-2.5000000000, 0.0000000000, 0.0000000000]) {
															color(c = "darkmagenta") {
																translate(v = [0, 0, 0.5000000000]) {
																	cube(center = true, size = [5, 5, 1]);
																}
															}
														}
													}
												}
												color(c = "orange") {
													translate(v = [0, 0, 0.5000000000]) {
														cylinder(r1 = 5, $fn = 32, h = 1, r = 5, center = true);
													}
												}
											}
											translate(v = [0.0000000000, 1.2500000000, 0.0000000000]) {
												translate(v = [-1.2500000000, 0.0000000000, 0.0000000000]) {
													color(c = "tomato") {
														translate(v = [0, 0, 0.5000000000]) {
															cylinder(r1 = 2.5000000000, $fn = 32, h = 1, r = 2.5000000000, center = true);
														}
													}
												}
											}
										}
									}
								}
							}
						}
					}
					translate(v = [15.0000000000, -20.0000000000, 0.0000000000]) {
						mirror(v = [1, 0, 0]) {
							translate(v = [-15.0000000000, 20.0000000000, -0.0000000000]) {
								translate(v = [15.0000000000, -20.0000000000, 0.0000000000]) {
									mirror(v = [0, 1, 0]) {
										translate(v = [-15.0000000000, 20.0000000000, -0.0000000000]) {
											color(c = "firebrick") {
												translate(v = [15, -20, 0]) {
													difference() {
														union() {
															difference() {
																color(c = "steelblue") {
																	translate(v = [0, 0, 0.5000000000]) {
																		cube(center = true, size = [10, 10, 1]);
																	}
																}
																translate(v = [0.0000000000, 2.5000000000, 0.0000000000]) {
																	translate(v = [-2.5000000000, 0.0000000000, 0.0000000000]) {
																		color(c = "darkmagenta") {
																			translate(v = [0, 0, 0.5000000000]) {
																				cube(center = true, size = [5, 5, 1]);
																			}
																		}
																	}
																}
															}
															color(c = "orange") {
																translate(v = [0, 0, 0.5000000000]) {
																	cylinder(r1 = 5, $fn = 32, h = 1, r = 5, center = true);
																}
															}
														}
														translate(v = [0.0000000000, 1.2500000000, 0.0000000000]) {
															translate(v = [-1.2500000000, 0.0000000000, 0.0000000000]) {
																color(c = "tomato") {
																	translate(v = [0, 0, 0.5000000000]) {
																		cylinder(r1 = 2.5000000000, $fn = 32, h = 1, r = 2.5000000000, center = true);
																	}
																}
															}
														}
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
				translate(v = [-15.0000000000, -20.0000000000, 0.0000000000]) {
					mirror(v = [0, 1, 0]) {
						translate(v = [15.0000000000, 20.0000000000, -0.0000000000]) {
							color(c = "teal") {
								translate(v = [-15, -20, 0]) {
									difference() {
										union() {
											difference() {
												color(c = "steelblue") {
													translate(v = [0, 0, 0.5000000000]) {
														cube(center = true, size = [10, 10, 1]);
													}
												}
												translate(v = [0.0000000000, 2.5000000000, 0.0000000000]) {
													translate(v = [-2.5000000000, 0.0000000000, 0.0000000000]) {
														color(c = "darkmagenta") {
															translate(v = [0, 0, 0.5000000000]) {
																cube(center = true, size = [5, 5, 1]);
															}
														}
													}
												}
											}
											color(c = "orange") {
												translate(v = [0, 0, 0.5000000000]) {
													cylinder(r1 = 5, $fn = 32, h = 1, r = 5, center = true);
												}
											}
										}
										translate(v = [0.0000000000, 1.2500000000, 0.0000000000]) {
											translate(v = [-1.2500000000, 0.0000000000, 0.0000000000]) {
												color(c = "tomato") {
													translate(v = [0, 0, 0.5000000000]) {
														cylinder(r1 = 2.5000000000, $fn = 32, h = 1, r = 2.5000000000, center = true);
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
			color(c = "saddlebrown") {
				translate(v = [-15, 20, 0]) {
					difference() {
						union() {
							difference() {
								color(c = "steelblue") {
									translate(v = [0, 0, 0.5000000000]) {
										cube(center = true, size = [10, 10, 1]);
									}
								}
								translate(v = [0.0000000000, 2.5000000000, 0.0000000000]) {
									translate(v = [-2.5000000000, 0.0000000000, 0.0000000000]) {
										color(c = "darkmagenta") {
											translate(v = [0, 0, 0.5000000000]) {
												cube(center = true, size = [5, 5, 1]);
											}
										}
									}
								}
							}
							color(c = "orange") {
								translate(v = [0, 0, 0.5000000000]) {
									cylinder(r1 = 5, $fn = 32, h = 1, r = 5, center = true);
								}
							}
						}
						translate(v = [0.0000000000, 1.2500000000, 0.0000000000]) {
							translate(v = [-1.2500000000, 0.0000000000, 0.0000000000]) {
								color(c = "tomato") {
									translate(v = [0, 0, 0.5000000000]) {
										cylinder(r1 = 2.5000000000, $fn = 32, h = 1, r = 2.5000000000, center = true);
									}
								}
							}
						}
					}
				}
			}
		}
		color(c = "springgreen") {
			translate(v = [0, 0, 0.5000000000]) {
				cube(center = true, size = [40, 30, 1]);
			}
		}
	}
	color(c = "teal") {
		translate(v = [0, 0, 0.5000000000]) {
			cube(center = true, size = [20, 50, 1]);
		}
	}
}